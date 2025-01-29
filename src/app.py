from fastapi import FastAPI, Query
import uvicorn
import json

app = FastAPI()

def load_books():
    with open("books.json", "r") as file:
        return json.load(file)

@app.get("/books")
def get_books(genre: str = Query(None), title: str = Query(None)):
    books = load_books()

    # Apply filtering logic based on query parameters
    if genre:
        books = [book for book in books if genre.lower() in book['genre'].lower()]
    if title:
        books = [book for book in books if title.lower() in book['title'].lower()]

    return books

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
