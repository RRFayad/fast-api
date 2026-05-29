import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
raw_db_url = os.getenv("SQLALCHEMY_DATABASE_URL") or ""

if raw_db_url.startswith("sqlite:///./"):
    sqlite_path = BASE_DIR / raw_db_url.removeprefix("sqlite:///./")
    SQLALCHEMY_DB_URL = f"sqlite:///{sqlite_path}"
else:
    SQLALCHEMY_DB_URL = raw_db_url

# Creates the engine - how SQLAlchemy interacts with the DB
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
# Config: the check_same_thread as False means there could be multiple threads running at the same time

# This creates a Session "factory", not a session yet
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Config: Standard - we bind to the engine, and avoid auto stuff

# All my ORM models inherit from here
Base = declarative_base()
