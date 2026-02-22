from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
]


@app.get("/books")
def read_all_books():  # We dont need to explicit the async, fastapi will handle it for us (but we could)
    return BOOKS


@app.get("/books/search")
# We can use query parameters to search for books by title or author
# This static route should comes before the dynamic route, otherwise it will be treated as a dynamic route and we will never reach the search endpoint
def search_books(query: str):
    results = []
    for book in BOOKS:
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            results.append(book)
    return results


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}
