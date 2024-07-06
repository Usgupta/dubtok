from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from db.database import SessionLocal, create_tables
import db.crud as crud
import db.schemas as schemas
import boto3
import uuid
from datetime import datetime
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv
import os
import shutil
from services.video_audio_processor import separate_audio_video, combine_audio_video

import sys
sys.path.append('../')

from ai.ai_service import dubbing 

# Creates the tables in the database if it is not already present
create_tables()

# Defines the FastAPI application
app = FastAPI()

# Interface with methods that map to AWS s3
s3 = boto3.client('s3')
BUCKET_NAME = 'tiktoktechjam-2024'

# Loads the environment file containing the OpenAI API key
load_dotenv()

# Obtains the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# Debug
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Video uploading
@app.post("/upload/", response_model=schemas.Video)
async def upload_video(file: UploadFile = File(...), dub_type: str = Form(...), db: Session = Depends(get_db)):
    # Unique id for each video
    video_id = str(uuid.uuid4())


    upload_directory = "../uploads"
    os.makedirs(upload_directory, exist_ok=True)  # Create the directory if it doesn't exist
    file_path = os.path.join(upload_directory, file.filename)

    # Save the uploaded file
    with open(file_path, "wb") as file_obj:
        shutil.copyfileobj(file.file, file_obj)

    filename = os.path.splitext(file.filename)[0]

    audio_file_path = f"../uploads/{filename}.mp3"
    noaudio_video_file_path = f"../uploads/{filename}_noaudio.mp4"

    separate_audio_video(file_path, audio_file_path,noaudio_video_file_path )
    
    dubbed_audio_file_path = dubbing(audio_file_path, dub_type, filename)

    dubbed_video_file_path = f'output/{filename}.mp4'

    combine_audio_video(noaudio_video_file_path,dubbed_audio_file_path, dubbed_video_file_path)

    try:

        # Upload the video into AWS s3
        s3.upload_fileobj(file.file, BUCKET_NAME, video_id + "/" + dub_type + "_" + file.filename)
        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{video_id}/{dub_type}_{file.filename}"
        
        # Creates a video record in the database
        db_video = crud.create_video(db, video_id, file.filename, datetime.now())
        return db_video
    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="AWS credentials not available")
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Video retrieval
@app.get("/videos/{video_id}", response_model=schemas.Video)
async def get_video(video_id: str, db: Session = Depends(get_db)):
    db_video = crud.get_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video
