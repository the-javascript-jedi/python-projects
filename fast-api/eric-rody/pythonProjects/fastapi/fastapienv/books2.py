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
    published_date: int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date
# pydantic class for validation
# import the basemode
class Bookrequest(BaseModel):
    id:Optional[int]=Field(title='id is not needed') #Optional means it can be a number or null
    title:str=Field(min_length=3)
    author:str=Field(min_length=1)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=0,lt=6)
    published_date:int=Field(gt=1999,lt=2031)
    # an example schema - specified inside the Bookrequest class
    class Config:
        schema_extra = {
            'example': {
                'title': 'A new Book',
                'author': 'codingwithroby',
                'author': 'codingwithroby',
                'description': 'A new description of a new book',
                'rating': 5,
                'published_date':2012
            }
        }

BOOKS=[
    Book(1,'Computer Science Pro','codingwithroby','A very nice book!',5,2007),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5,2007),
    Book(3, 'Master Endpoints', 'codingwithroby', 'An awesome book', 5,2009),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2,2009),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3,2012),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1,2016),
]

@app.get("/books")
async def read_all_books():
    return BOOKS
# find book by id - using path params
@app.get("/books/{book_id}")
# http://127.0.0.1:8000/books/1
async def read_book(book_id:int):
    for book in BOOKS:
        if book.id==book_id:
            return book
#  find book by rating - using query params
@app.get("/books/")
#  http://127.0.0.1:8000/books/?book_rating=5
async def read_book_by_rating(book_rating:int):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==book_rating:
            books_to_return.append(book)
    return books_to_return

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

# update book with PUT request
@app.put("/books/update_book")
async def update_book(book:Bookrequest):
    for i in range(len(BOOKS)):
        if(BOOKS[i]).id==book.id:
            BOOKS[i]=book

#delete book
@app.delete("/books/{book_id}")
async def delete_book(book_id:int):
    for i in range(len(BOOKS)):
        if(BOOKS[i]).id==book_id:
            BOOKS.pop(i)
            break

# filter by published data - using path parameters
@app.get("/books/filter/{published_date}")
async def filter_by_date(published_date:int):
    print("published_date",published_date)
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return