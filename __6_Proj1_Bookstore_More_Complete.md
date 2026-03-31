## Bookstore Proj

- Now we going to create a more compelte API, including:
  - CRUD
  - Data Validation, Exception Handling, Status Codes, Swagger Config, Python Req Objects

### Pydanticts & Data Valdiation

- Pydantics is for: Data Validation, data modeling, data aprsing, error handling

- So the logic is:
  - Create Pydantic Request Model (like Zod probably, whic could be translated to the Books class);
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

- We can also add model_config to create a more descriptive request in our Swagger docs

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
