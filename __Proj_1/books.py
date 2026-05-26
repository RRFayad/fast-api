from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
    #   {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
]


@app.get("/books")
def read_all_books():  # We dont need to explicit the async, fastapi will handle it for us (but we could)
    return BOOKS


@app.get("/books/search")
# We can use query parameters to search for books by title or author
# This static route should comes before the dynamic route, otherwise it will be treated as a dynamic route and we will never reach the search endpoint
def search_books(query: str = None):
    if not query:
        return BOOKS
    results = []
    for book in BOOKS:
        if query.casefold() in book["title"].casefold() or query.casefold() in book["author"].casefold():
            results.append(book)
    return results


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}


@app.post("/books")
def create_book(new_book: dict = Body()):

    new_book["id"] = len(BOOKS) + 1
    BOOKS.append(
        new_book
    )
    return {"Prev": BOOKS[:-1], "UPDATED": BOOKS}


@app.put("/books")
def update_book_by_id(updated_book: dict = Body()):
    for book in BOOKS:
        if book["id"] == updated_book["id"]:
            book["title"] = updated_book["title"]
            book["author"] = updated_book["author"]
            return {"Updated:": book}


@app.delete("/books")
def delete_book_by_id(id: int = Body()):
    print(id)
    for i in range(0, len(BOOKS)-1):
        if BOOKS[i]["id"] == id:
            deleted = BOOKS[i]
            BOOKS.pop(i)
            return {"Deleted item:": f"{deleted}"}
    return {"Failed - Item not found"}
