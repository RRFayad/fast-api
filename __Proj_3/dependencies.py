from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status
from jose import JWTError, jwt

from __Proj_3.constants import JWT_ALGORITHM, JWT_SECRET_KEY

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

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


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

        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


user_dependency = Annotated[dict, Depends(get_current_user_from_token)]
