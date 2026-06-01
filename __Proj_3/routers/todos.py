from typing import Annotated

from fastapi import APIRouter, HTTPException, Path
from fastapi.params import Depends
from pydantic import BaseModel, Field
from starlette import status


from ..dependencies import db_dependency, user_dependency
from ..models import Todos

router = APIRouter(prefix="/todo", tags=["todo"])


class TodoReq(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(max_length=100)
    priority: int = Field(ge=1, le=5)
    complete: bool = False


@router.get("/", status_code=status.HTTP_200_OK)
def read_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return db.query(Todos).filter(Todos.owner == user.get("id")).all()


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_todo_by_id(user: user_dependency, db: db_dependency, id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    todo_item = (
        db.query(Todos).filter(Todos.id == id, Todos.owner == user.get("id")).first()
    )
    if todo_item is not None:
        return todo_item
    raise HTTPException(status_code=404, detail="Todo not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(user: user_dependency, db: db_dependency, todoReq: TodoReq):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")

    if todoReq is not None:
        try:
            todo_model = Todos(
                title=todoReq.title,
                description=todoReq.description,
                priority=todoReq.priority,
                complete=todoReq.complete,
                owner=user.get("id"),
            )
            db.add(todo_model)
            db.commit()
            db.refresh(todo_model)
            return todo_model
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Error creating todo")
    raise HTTPException(status_code=400, detail="Invalid todo data")


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_todo(
    user: user_dependency,
    db: db_dependency,
    todoReq: TodoReq,
    id: int = Path(gt=0),
):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    todo_item = (
        db.query(Todos).filter(Todos.id == id, Todos.owner == user.get("id")).first()
    )
    if todo_item is not None:
        todo_item.title = todoReq.title
        todo_item.description = todoReq.description
        todo_item.priority = todoReq.priority
        todo_item.complete = todoReq.complete
        db.add(todo_item)
        db.commit()
        return
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(user: user_dependency, db: db_dependency, id: int = Path(gt=0)):
    to_be_deleted_item = (
        db.query(Todos).filter(Todos.id == id, Todos.owner == user.get("id")).first()
    )
    if to_be_deleted_item is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(to_be_deleted_item)
    db.commit()
