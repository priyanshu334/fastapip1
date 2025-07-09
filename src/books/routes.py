from fastapi import APIRouter ,status
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from src.books.schemas import Book,Book_update_model
from typing import List

book_router= APIRouter()


@book_router.get("/")
async def Home():
    return "hello"

@book_router.get("/books",response_model=List[Book])
async def get_all_books():
    return books

@book_router.post("/books",status_code=status.HTTP_201_CREATED)
async def create_a_book(book:Book)->dict:
    books.append(book.dict())
    return {"message":"Book added sucessfully"}

  
  

@book_router.get("/book/{book_id}")
async def get_book(book_id:int)->dict:
    for book in books:
        if book['id'] == book_id:
            return book
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@book_router.put("/book/{book_id}")
async def update_a_book(book_id:int,book_update_data:Book_update_model)->dict:
    for book in books:
        if book['id']== book_id:
            book['title']= book_update_data.title
            book["publisher"]= book_update_data.publisher
            book["author"]= book_update_data.author
            book["page_count"] = book_update_data.page_count
            book['language']= book_update_data.language
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        



@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            

        
