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

```python
    load_dotenv()

    SQLALCHEMY_DB_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

    # There could be multiple threads running at the same time
    engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})

    # Standard - so we bind to the engine, and avoid auto stuff
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()
```

### Create Models

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
