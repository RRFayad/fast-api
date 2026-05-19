## Bookstore Proj

- Now we going to create a more compelte API, including:
  - CRUD
  - Data Validation, Exception Handling, Status Codes, Swagger Config, Python Req Objects

### Pydanticts & Data Valdiation

- Pydantics is for: Data Validation, data modeling, data aprsing, error handling

- So the logic is:
  - Create Pydantic Request Model (like Zod, whic could be translated to the Books class);
  - Field data validation on each variable;
  - Convert the Pydantic object into the Book, after validation

#### Data Validation

- Obs.:
  - Attention that the validation goes in the Req Body, not the final object class
  - I already returns error messages

```python
  class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)

  def create_book(book_req: BookRequest):
      #...
```

- **Obs.: **We can also add model_config to create a more descriptive request in our Swagger docs

#### Path Validation

- We can use **Path** to validate the parameter (or it will automatically return an error) (or **Query** for query params)

```python
  @app.get("/books/{book_id}")
  def get_book_by_id(book_id: int = Path(gt=0)):
  # ...


@app.get("/books/publish_year/")
def get_books_by_publish_year(publish_year: int = Query(ge=1900, le=2020)):
  # ...

```

#### Status Codes Overview

- 1xx: Req Processing
- 2xx: Success
  - 200: Ok
  - 201: Created
  - 204: No Content (Usually a PUT - didnt create nor return)
- 3xx - Frther action must be complete
- 4xx - Client Errors
  - 400: Bad Request
  - 401: Unauthorized
  - 404: Not FOund
  - 422: Unprocessable Entity
- 5xx - Server Side Errors
  - 500: Internal server error

### Add HTTP Codes in the response

```python
  @app.get("/books", status_code=status.HTTP_200_OK)
  def read_all_books():
    return BOOKS

  @app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_book_by_id(book_id: int):
        for book in BOOKS:
        if book.id == book_id:
            BOOKS.remove(book)
            return {"Deleted:": book}
    raise HTTPException(status_code=404, detail="Book not found")
```

#### HTTP Exceptions

```python
  @app.get("/books/{book_id}")
  def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
  raise HTTPException(status_code=404, detail="Book not found")
```

### Notes / Obs during course:

- ternary operator:
  `book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1`

- use of `**` in Python:
  - It is used for packing and unpacking kwargs

  ```python

    def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

      details = {"name": "Alice", "age": 30}

      # Unpacks the dictionary into name="Alice", age=30
      intro(**details)
      # Output: My name is Alice and I am 30 years old.


  ```
