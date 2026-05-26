import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# There could be multiple threads running at the same time
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})

# Standard - so we bind to the engine, and avoid auto stuff
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
