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

```python
  class Todos(Base):
    __tablename__ = "todos"

    # Primary key = Unique Identifier; Index = auto generate indexing
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
```

### SQLite

- After installing SQLite, we can use it from the terminal.
  - **Obs.:** To make the return more readable we can enter `.mode table` (table is the one I liked most)
  - Some mode examples: `column`, `markdown`, `box`, `table`

- With the current setup, the database is stored in a .db file that can be opened with SQLite.

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
