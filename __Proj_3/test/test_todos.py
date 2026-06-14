import os

from sqlalchemy import create_engine
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "sqlite:///./testdb.db"
os.environ["SQLALCHEMY_DATABASE_URL"] = SQLALCHEMY_DB_URL

from __Proj_3.main import app
from __Proj_3.database import Base
from __Proj_3.dependencies import CurrentUser, get_current_user_from_token, get_db

engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return CurrentUser(username="test", id=1, role="admin")


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user_from_token] = override_get_current_user

client = TestClient(app)


def test_read_all_authenticated():
    response = client.get("/todo/")
    assert response.status_code == status.HTTP_200_OK
