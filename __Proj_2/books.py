from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, publish_year: int, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.publish_year = publish_year
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(
        description="The unique identifier for the book. This field is optional and will be auto-generated if not provided.", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    publish_year: int = Field(ge=0, le=9999)
    rating: int = Field(ge=1, le=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book title",
                "author": "An author name",
                "description": "A brief description of the book.",
                "publish_year": 2023,
                "rating": 5
            }
        }
    }


BOOKS = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald",
         description="A novel set in the Roaring Twenties, exploring themes of wealth, love, and the American Dream.", publish_year=1925, rating=5),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee",
         description="A novel about racial injustice in the Deep South, seen through the eyes of a young girl.", publish_year=1960, rating=5),
    Book(id=3, title="1984", author="George Orwell",
         description="A dystopian novel that explores themes of totalitarianism, surveillance, and individuality.", publish_year=1949, rating=4),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen",
         description="A classic novel that delves into themes of love, class, and societal expectations.", publish_year=1813, rating=5),
]


def insert_id_in_book(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.get("/books", status_code=status.HTTP_200_OK)
def read_all_books():
    return BOOKS


@app.get("/books/rating/{rating}", status_code=status.HTTP_200_OK)
def get_books_by_rating(rating: int):
    books = [book for book in BOOKS if book.rating == rating]
    if books:
        return books
    return {"error": "No books found with the specified rating"}


@app.get("/books/publish_year/", status_code=status.HTTP_200_OK)
def get_books_by_publish_year(publish_year: int = Query(ge=1900, le=2020)):
    books = [book for book in BOOKS if book.publish_year == publish_year]
    if books:
        return books
    raise HTTPException(
        status_code=404, detail="No books found with the specified publish year")


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book_req: BookRequest):
    # print(book_req ). # It shows that book_req is an instance of BookRequest;

    # ** unpack and pack key values, so new_book["id"] = book_req["id"] etc
    new_book = Book(**book_req.model_dump())
    new_book = insert_id_in_book(new_book)
    BOOKS.append(new_book)

    return {"Added:": new_book}


@app.put("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_book_by_id(book_req: BookRequest):
    for index in range(len(BOOKS)):
        if BOOKS[index].id == book_req.id:
            BOOKS[index].title = book_req.title
            BOOKS[index].author = book_req.author
            BOOKS[index].description = book_req.description
            BOOKS[index].rating = book_req.rating
            BOOKS[index].publish_year = book_req.publish_year

            return {"Updated:": BOOKS[index]}
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            BOOKS.remove(book)
            return {"Deleted:": book}
    raise HTTPException(status_code=404, detail="Book not found")
