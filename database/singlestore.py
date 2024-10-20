import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Candidate(Base):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    resume = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Interview(Base):
    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, nullable=False)
    job_id = Column(Integer, nullable=False)
    status = Column(String(50), default='scheduled')
    scheduled_at = Column(DateTime)
    completed_at = Column(DateTime)
    result = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

engine = create_engine(os.getenv('SINGLESTORE_CONNECTION_STRING'))
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def get_session():
    return Session()