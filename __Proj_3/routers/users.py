import bcrypt
from starlette import status
from fastapi import APIRouter, HTTPException

from ..dependencies import db_dependency, user_dependency
from ..models import Users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_user_info(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return db.query(Users).filter(Users.id == user.id).first()


@router.put("/update-password", status_code=status.HTTP_200_OK)
def update_password(user: user_dependency, db: db_dependency, new_password: str):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    user_row = db.query(Users).filter(Users.id == user.id).first()
    if user_row is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    user_row.hashed_password = bcrypt.hashpw(
        new_password.encode("utf-8"), bcrypt.gensalt(14)
    ).decode("utf-8")
    try:
        db.add(user_row)
        db.commit()
        db.refresh(user_row)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create user",
        )
