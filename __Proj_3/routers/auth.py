from datetime import datetime, timedelta, timezone

import token

import bcrypt
from jose import JWTError, jwt
from starlette import status
from typing import Annotated

from pydantic import BaseModel
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette.status import (
    HTTP_201_CREATED,
)

from __Proj_3.constants import JWT_ALGORITHM, JWT_SECRET_KEY

from ..dependencies import db_dependency
from ..models import Users

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


def create_access_token(
    username: str, user_id: int, role: str, expires_delta: timedelta
):
    if not JWT_SECRET_KEY:
        raise ValueError("NO JWT_SECRET_KEY env var provided")
    encode = {"sub": username, "id": user_id, "role": role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create user",
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
    token = create_access_token(
        user.username, user.id, user.role, timedelta(minutes=60)
    )
    return {"access_token": token, "token_type": "bearer"}
