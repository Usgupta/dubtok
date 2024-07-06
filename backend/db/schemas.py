from pydantic import BaseModel
from datetime import datetime

# Base class which defines the attributes the video table has
class VideoBase(BaseModel):
    video_id: str
    filename: str
    upload_date: datetime

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    class Config:
        orm_mode = True
