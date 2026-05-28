from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import Todos

router = APIRouter()


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


class TodoReq(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(max_length=100)
    priority: int = Field(ge=1, le=5)
    complete: bool = False


@router.get("/", status_code=status.HTTP_200_OK)
def read_all(db: db_dependency):
    return db.query(Todos).all()


@router.get("/todo/{id}", status_code=status.HTTP_200_OK)
def get_todo_by_id(db: db_dependency, id: int = Path(gt=0)):
    todo_item = db.query(Todos).filter(Todos.id == id).first()
    if todo_item is not None:
        return todo_item
    raise HTTPException(status_code=404, detail="Todo not found")


@router.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(db: db_dependency, todoReq: TodoReq):
    if todoReq is not None:
        try:
            todo_model = Todos(
                title=todoReq.title,
                description=todoReq.description,
                priority=todoReq.priority,
                complete=todoReq.complete,
            )
            db.add(todo_model)
            db.commit()
            return
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Error creating todo")
    raise HTTPException(status_code=400, detail="Invalid todo data")


@router.put("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_todo(
    db: db_dependency,
    todoReq: TodoReq,
    id: int = Path(gt=0),
):
    todo_item = db.query(Todos).filter(Todos.id == id).first()
    if todo_item is not None:
        todo_item.title = todoReq.title
        todo_item.description = todoReq.description
        todo_item.priority = todoReq.priority
        todo_item.complete = todoReq.complete
        db.add(todo_item)
        db.commit()
        return
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(db: db_dependency, id: int = Path(gt=0)):
    to_be_deleted_item = db.query(Todos).filter(Todos.id == id).first()
    if to_be_deleted_item is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(to_be_deleted_item)
    db.commit()
