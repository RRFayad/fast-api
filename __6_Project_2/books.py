from fastapi import Body, FastAPI

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int = None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


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


@app.get("/books")
def read_all_books():
    return BOOKS


@app.post("/books")
def create_book(book_req=Body()):

    BOOKS.append(book_req)
    return {"Added:": book_req}
