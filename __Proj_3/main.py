from fastapi import FastAPI

from . import models
from .database import engine
from .routers import admin, auth, todos

app = FastAPI()

# Its ran only when there is no db
models.Base.metadata.create_all(bind=engine)

app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(todos.router)
