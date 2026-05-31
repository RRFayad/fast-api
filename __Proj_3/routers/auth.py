from datetime import datetime, timedelta, timezone
import os
import token

import bcrypt
from jose import JWTError, jwt
from starlette import status
from typing import Annotated
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_401_UNAUTHORIZED,
)

from ..dependencies import db_dependency
from ..models import Users

load_dotenv()
JWT_SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ALGORITHM = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

router = APIRouter(prefix="/auth", tags=["auth"])


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str


def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return None
    if not bcrypt.checkpw(
        password=password.encode("utf-8"),
        hashed_password=user.hashed_password.encode("utf-8"),
    ):
        return None
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    if not JWT_SECRET_KEY:
        raise ValueError("NO JWT_SECRET_KEY env var provided")
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc)
    encode.update({"exp": expires})
    return jwt.encode(encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


async def get_current_user_from_token(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY or "", algorithms=JWT_ALGORITHM)
        username: str | None = payload.get("sub")
        user_id: int | None = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )

        return {"username": username, "user_id": user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


@router.post("/", status_code=HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_req: CreateUserRequest):

    user_model = Users(
        email=create_user_req.email,
        username=create_user_req.username,
        first_name=create_user_req.first_name,
        last_name=create_user_req.last_name,
        role=create_user_req.role,
        hashed_password=bcrypt.hashpw(
            create_user_req.password.encode("utf-8"),
            bcrypt.gensalt(14),
        ).decode("utf-8"),
        is_active=True,
    )

    try:
        db.add(user_model)
        db.commit()
        db.refresh(user_model)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    token = create_access_token(user.username, user.id, timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}
