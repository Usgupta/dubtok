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