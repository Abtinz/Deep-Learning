"""
Database setup and models for image storage
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Database configuration
DATABASE_DIR = "data"
DATABASE_FILE = os.path.join(DATABASE_DIR, "images.db")
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

# Create database directory if it doesn't exist
os.makedirs(DATABASE_DIR, exist_ok=True)

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ImageRecord(Base):
    """Database model for storing image metadata"""
    __tablename__ = "images"
    
    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String, nullable=False, index=True)
    image_path = Column(String, nullable=False)
    model_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)


def init_db():
    """Initialize database and create tables"""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

