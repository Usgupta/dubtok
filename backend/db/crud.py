from sqlalchemy.orm import Session
from db.models import Video
from datetime import datetime

# Gets the video record from the database
def get_video(db: Session, video_id: int):
    return db.query(Video).filter(Video.video_id == video_id).first()

# Creates a video record in the database
def create_video(db: Session, video_id: str, filename: str, upload_date: datetime):
    db_video = Video(video_id=video_id, filename=filename, upload_date=upload_date)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video