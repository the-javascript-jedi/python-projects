from typing import Optional
#  to run app - uvicorn books2:app --reload
from fastapi import FastAPI,Body
# pydantic used for data validation comes with fast api
# import Field to add validation for each field
from pydantic import BaseModel,Field


app=FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
# pydantic class for validation
# import the basemode
class Bookrequest(BaseModel):
    id:Optional[int] #Optional means it can be a number or null
    title:str=Field(min_length=3)
    author:str=Field(min_length=1)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=0,lt=6)

BOOKS=[
    Book(1,'Computer Science Pro','codingwithroby','A very nice book!',5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome book', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post ("/create-book")
# use pyDantic class for type validation
async def create_book(book_request:Bookrequest):
    print('type(Bookrequest)--before',type(Bookrequest))
    #print output - <class 'pydantic.main.ModelMetaclass'>
    # **book_request.dict() converts the request to Book object
    # expand dictionary and returm the key value pairs
    new_book=Book(**book_request.dict())
    print('type(new_book)--after',type(new_book))
    #print output - <class 'books2.Book'>
    # append an id to the book value
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):
    # if len(BOOKS)>0:
    #     # Books[-1] - selects the last value
    #     book.id=BOOKS[-1].id+1
    # else:
    #     book.id=1
    # ternary operator
    book.id=1 if len(BOOKS)==0 else BOOKS[-1].id+1
    return book