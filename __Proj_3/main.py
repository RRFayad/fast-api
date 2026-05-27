import models
from models import Todos
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from database import engine, SessionLocal

app = FastAPI()

# Its ran only when there is no db
models.Base.metadata.create_all(bind=engine)


def get_db():
    """
    This function manages the db lifecycle, by:
    1. Creating a session;
    2. Injecting it to the endpoint
    3. Cleaning up after request finishes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Depends is a FastAPI Dependency Injection - which means, determine this value by running the function when its called
db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
def read_all(db: db_dependency):
    return db.query(Todos).all()
