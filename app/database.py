import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://user:password@127.0.0.1:5432/hh_db')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def get_session():
    return SessionLocal()