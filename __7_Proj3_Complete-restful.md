## Project 3

- We will work with Todos in a Todo Table

- New Skills:
  - Full SQL Database
  - Authentication with JWTs
  - Authorization
  - Hashing Passoword

### Setup Dataabse

- ![DB Table:](/__Proj_3/assets/todo_table.png)

- DBMS - Database Management Systems - e.g.: SQLite, MySQL and PostgreSQL

- install sqlalchemy

- The core concept for the DB Setup are:
  - The core concepts from the db setup and its implementation here are:
    1. We created the engine (how SQLAlchemy talsk to the DB) by `engine = create_engine(SQLALCHEMY_DB_URL)`
    2. We created a Session "factory", not a session yet, by `SessionLocal = sessionmaker(bind=engine)`
    3. Determined that all models are inherited from a 'Base' model, by `Base = declarative_base()`

```python
    load_dotenv()

    SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# Creates the engine - how SQLAlchemy interacts with the DB
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})

# This creates a Session "factory", not a session yet
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All my ORM models inherit from here
Base = declarative_base()
```

### Create Models

- We can see, that as mentionen in step 3 above, all models are inherited from Base
  - **Obs.:** Updated for the new SQLAlchemy way of doing, with strong type inference. So its different from the course

```python
class Todos(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # Primary key = Unique Identifier; Index = auto generate indexing
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    priority: Mapped[int] = mapped_column()
    complete: Mapped[bool] = mapped_column(default=False)
    owner: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
```

### SQLite

- After installing SQLite, we can use it from the terminal.
  - **Obs.:** To make the return more readable we can enter `.mode table` (table is the one I liked most)
  - Some mode examples: `column`, `markdown`, `box`, `table`

- With the current setup, the database is stored in a .db file that can be opened with SQLite.
  - `sqlite3 database.py`

### Start FastAPI

- Now, in our FastAPI, we create a db lifecycle management, by:
  1. Creating a session;
  2. Injecting it to the endpoint
  3. Cleaning up after request finishes
  - **Obs.:** This is why Depency Injection is important in the requests, e.g.:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

  @app.get("/")
  def read_all(db: Annotated[Session, Depends(get_db)]): # Depends is a FastAPI Dependy Injection
    return db.query(Todos).all()
```

### Add Routers

- By adding routes, this is the main file:

```python
  app = FastAPI()

  # Its ran only when there is no db
  models.Base.metadata.create_all(bind=engine)

  app.include_router(auth.router)
  app.include_router(todos.router)
```

- And this it the `/routers/auth.py`:

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/auth")
async def get_user():
    pass
```

### SQLAlchemy Notes / Syntax

- select all:
  `db.query(Todos).all()`

- select first match:
  `db.query(Todos).filter(Todos.id == id).first()`

- filter multiple conditions:
  `db.query(Todos).filter(Todos.complete == False, Todos.priority > 2).all()`

- create item:
  `db.add(todo)`

- commit changes:
  `db.commit()`

- refresh object from DB:
  `db.refresh(todo)`

- update object:
  `todo.title = "New title"`

- delete object:
  `db.delete(todo)`

- order by:
  `db.query(Todos).order_by(Todos.priority.desc()).all()`

- limit results:
  `db.query(Todos).limit(5).all()`

## Authentication

- First we are going to create a Users Table, which will have One to Many Relationship with ToDos
  - So in our ToDo app, each todo will have a owner FK (foreign key) which will reference an user
