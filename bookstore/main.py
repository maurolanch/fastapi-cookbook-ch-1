from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class BookResponse(BaseModel):
    title: str
    author: str


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id":book_id,
        "title":"The Great Gatsby",
        "author":"F. Scott Fitzgerald"
    }


@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        "author_id": author_id,
        "author_name":"Ernest Hemingway"
    }

@app.get("/books")
async def read_books(year: int = None):
    if year:
        return {
                "year": year,
                "books":["Book 1", "Book 2"]
        }
    return {
        "books":["All Books"]
    }

@app.get("/allbooks")
async def read_all_books() -> list[BookResponse]:
    return [
        {
            "id":1,
            "title":"1984",
            "author":"George Orwell"
        },
        {
            "id":1,
            "title":"The Great Gatsby",
            "author":"F. Scott Fitzgerald" 
        }
    ]

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message":"Oops! Something went wrong"
        }
    )