import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DATABASE_URL") or ""

# Creates the engine - how SQLAlchemy interacts with the DB
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
# Config: the check_same_thread as False means there could be multiple threads running at the same time

# This creates a Session "factory", not a session yet
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Config: Standard - we bind to the engine, and avoid auto stuff

# All my ORM models inherit from here
Base = declarative_base()
