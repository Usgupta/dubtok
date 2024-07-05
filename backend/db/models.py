from sqlalchemy import Column, String, TIMESTAMP
from db.database import Base

# Creates a Video model which effectively maps to the "videos" table in the database using ORM
class Video(Base):
    # Name of the table
    __tablename__= "videos"
    
    # Columns in the table
    video_id = Column(String, primary_key=True, index=True)
    filename = Column(String)
    upload_date = Column(TIMESTAMP)