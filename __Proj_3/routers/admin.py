from typing import Annotated

from fastapi import APIRouter, HTTPException, Path
from fastapi.params import Depends
from pydantic import BaseModel, Field
from starlette import status


from ..dependencies import db_dependency, user_dependency
from ..models import Todos

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/todo", status_code=status.HTTP_200_OK)
def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.role != "admin":
        raise HTTPException(status_code=401, detail="Authentication failed")
    return db.query(Todos).all()


@router.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_by_id(user: user_dependency, db: db_dependency, id: int = Path(gt=0)):
    if user is None or user.role != "admin":
        raise HTTPException(status_code=401, detail="Authentication failed")
    db.query(Todos).filter(Todos.id == id).delete()
    db.commit()
