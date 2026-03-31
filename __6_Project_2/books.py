from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


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
    id: Optional[int] = Field(
        description="The unique identifier for the book. This field is optional and will be auto-generated if not provided.", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book title",
                "author": "An author name",
                "description": "A brief description of the book.",
                "rating": 5
            }
        }
    }


BOOKS = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald",
         description="A novel set in the Roaring Twenties, exploring themes of wealth, love, and the American Dream.", rating=5),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee",
         description="A novel about racial injustice in the Deep South, seen through the eyes of a young girl.", rating=5),
    Book(id=3, title="1984", author="George Orwell",
         description="A dystopian novel that explores themes of totalitarianism, surveillance, and individuality.", rating=4),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen",
         description="A classic novel that delves into themes of love, class, and societal expectations.", rating=5),
]


def insert_id_in_book(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.get("/books")
def read_all_books():
    return BOOKS


@app.post("/books")
def create_book(book_req: BookRequest):
    # print(book_req ). # It shows that book_req is an instance of BookRequest;

    # ** unpack and pack key values, so new_book["id"] = book_req["id"] etc
    new_book = Book(**book_req.model_dump())
    new_book = insert_id_in_book(new_book)
    BOOKS.append(new_book)

    return {"Added:": new_book}
