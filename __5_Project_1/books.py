from fastapi import FastAPI

app = FastAPI()


@app.get("/books")
def first_api():  # We dont need to explicit the async, fastapi will handle it for us (but we could)
    return {"message": "Hello, World!"}
