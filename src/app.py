from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

def load_books():
    with open("books.json", "r") as file:
        return json.load(file)

@app.get("/books")
def get_books():
    books = load_books()
    return books

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
