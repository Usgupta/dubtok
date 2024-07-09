from services.cleanup_temporary_files import cleanup_temporary_files
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
from fastapi.middleware.cors import CORSMiddleware
import re
import sys
# Add the root directory to the Python path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
sys.path.append('../')

from ai.ai_service import dubbing


# Creates the tables in the database if it is not already present
create_tables()

# Defines the FastAPI application
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "https://dubtok-forked.vercel.app",
    "https://dubtok-forked.vercel.app/demo",
    "https://dubtok-forked.vercel.app/",
    "https://dubtok-forked.vercel.app/demo/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Interface with methods that map to AWS s3

session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
s3 = session.client('s3')

# s3 = boto3.client('s3')
BUCKET_NAME = 'tiktoktechjam-2024'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Loads the environment file containing the OpenAI API key
load_dotenv()

def reformat_filename(filename):
    # Remove any leading or trailing whitespace
    filename = filename.strip()
    
    # Separate the filename and extension
    if '.' in filename:
        base, extension = filename.rsplit('.', 1)
    else:
        base, extension = filename, ''

    # Replace spaces and special characters in the base name with underscores
    base = re.sub(r'[^\w-]', '_', base)

    # Reconstruct the filename
    reformatted = f'{base}.{extension}' if extension else base

    return reformatted

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

    # Creates uploads directory containing video file uploads used for local processing if it doesn't exist
    upload_directory = "../uploads"
    os.makedirs(upload_directory, exist_ok=True) 

    reformatted_filename = reformat_filename(file.filename)

    # print(f'REFORMATED TO {reformatted_filename} from {file.filename}')

    file_path = os.path.join(upload_directory, reformatted_filename)

    print(f'saved to {file_path}')

    # Save the uploaded file
    with open(file_path, "wb") as file_obj:
        shutil.copyfileobj(file.file, file_obj)
        
    filename = os.path.splitext(reformatted_filename)[0]
    audio_file_path = f"../uploads/{filename}.mp3"
    noaudio_video_file_path = f"../uploads/{filename}_noaudio.mp4"
    # audio_file_path = os.path.join(BASE_DIR,f"../uploads/{filename}.mp3")
    # noaudio_video_file_path = os.path.join(BASE_DIR,f"../uploads/{filename}_noaudio.mp4")
    try: 
        # Separate the audio from the video file
        separate_audio_video(file_path, audio_file_path, noaudio_video_file_path)

        # Dubs the audio 
        dubbed_audio_file_path = dubbing(audio_file_path, dub_type, filename)

        # Mixes the dubbed audio to the video to get the final output 

        dubbed_video_file_path = os.path.join(BASE_DIR,f"output/{filename}.mp4")
        
        combine_audio_video(noaudio_video_file_path,dubbed_audio_file_path, filename)
    except Exception as e: 
        print(e)
        raise HTTPException(status_code=500, detail = str(e))

    try:

        # Upload the video into AWS s3
        s3.upload_file(dubbed_video_file_path, BUCKET_NAME, video_id + "/" + dub_type + "_" + filename + ".mp4")
        # file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{video_id}/{dub_type}_{filename}"

        # Creates a video record in the database
        db_video = crud.create_video(db, video_id, filename+".mp4", datetime.now())
        
        # Cleans up the temporary files generated during the dubbing process
        cleanup_temporary_files()
        
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
