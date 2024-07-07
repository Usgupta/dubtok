from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get the current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Setup for connecting to sqlite database
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'videos.db')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class required for each ORM model
Base = declarative_base()
    
# Creates the tables in the database if it is not already present
def create_tables():
    Base.metadata.create_all(bind=engine)