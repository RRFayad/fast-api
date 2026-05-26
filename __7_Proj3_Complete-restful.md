## Project 3

- We will work with Todos in a Todo Table

- New Skills:
  - Full SQL Database
  - Authentication with JWTs
  - Authorization
  - Hashing Passoword

### Setup Dataabse

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
