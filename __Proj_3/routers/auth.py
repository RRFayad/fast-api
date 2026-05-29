import bcrypt
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from starlette import status
from starlette.status import HTTP_201_CREATED

from ..dependencies import db_dependency
from ..models import Users

router = APIRouter()


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str


@router.post("/auth", status_code=HTTP_201_CREATED)
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
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
