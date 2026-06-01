from typing import Annotated
from starlette import status
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from __Proj_3.constants import JWT_ALGORITHM, JWT_SECRET_KEY

from .database import SessionLocal


class CurrentUser(BaseModel):
    username: str
    id: int
    role: str


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

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_current_user_from_token(
    token: Annotated[str, Depends(oauth2_bearer)],
):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY or "", algorithms=JWT_ALGORITHM)
        username: str | None = payload.get("sub")
        user_id: int | None = payload.get("id")
        role: str | None = payload.get("role")
        if username is None or user_id is None or role is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )

        return CurrentUser(username=username, id=user_id, role=role)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


user_dependency = Annotated[CurrentUser, Depends(get_current_user_from_token)]
