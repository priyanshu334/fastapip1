from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet")
async def greet(name:Optional[str]="User",age: int=0)->dict:
    return {"message": f"Hello, {name}! You are {age} years old."}

class Book(BaseModel):
    title:str
    author:str
@app.post("/create_book")
async def create_book(book: Book):
    return {"message": f"Book '{book.title}' by {book.author} created successfully."}