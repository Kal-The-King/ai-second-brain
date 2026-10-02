from sqlalchemy import Column, String, Text, DateTime, Float, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Memory(Base):
    __tablename__ = "memories"
    id = Column(String, primary_key=True, index=True)
    text = Column(Text)
    category = Column(String, default="general")
    source = Column(String, default="user")
    tags = Column(JSON, default=[])
    embedding = Column(JSON, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    importance_score = Column(Float, default=0.5)
    access_count = Column(String, default="0")


class WebCache(Base):
    __tablename__ = "web_cache"
    id = Column(String, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    content = Column(Text)
    summary = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    source_quality = Column(Float, default=0.5)


class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    preferences = Column(JSON, default={})
    goals = Column(JSON, default=[])
    style = Column(String, default="balanced")
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)
