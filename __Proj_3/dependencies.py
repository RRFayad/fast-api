from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from .database import SessionLocal


def get_db():
    """
    Manage the database session lifecycle for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
