from fastapi import Body, FastAPI
app=FastAPI()
# run the app -  uvicorn books:app --reload

BOOKS=[
    {'title': 'Title One', 'author': "Author One", "category":"science"},
    {'title': 'Title Two', 'author': "Author Two", "category": "science"},
    {'title': 'Title Three', 'author': "Author Three", "category": "history"},
    {'title': 'Title Four', 'author': "Author Four", "category": "math"},
    {'title': 'Title Five', 'author': "Author Five", "category": "math"},
    {'title': 'Title Six', 'author': "Author Six", "category": "math"},
    {'title': 'Title Seven', 'author': "Author Six", "category": "english"},
    {'title': 'Title Eight', 'author': "Author Six", "category": "tamil"},
]
# if api endpoint is repeated make sure the dynamic param is below the static param or the static value will never get executed

# read all books
@app.get("/books")
async def read_all_books():
    return BOOKS

# Dynamic Param
@app.get("/books/{book_title}")
# the dynamic param will be changed to a string eg number 1 becomes string "1"
async def read_book(book_title:str):
    for book in BOOKS:
        # casefold makes string lowercase
        if book.get('title').casefold()==book_title.casefold():
            return book
# search book by category
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return=[]
    for book in BOOKS:
        print("book",book)
        if(book.get('category').casefold()==category.casefold()):
            books_to_return.append(book)
    return books_to_return
#  search book by author and category
#  path param to find location
#  query params to filter what we want to return
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str,category:str):
    books_to_return=[]
    for book in BOOKS:
        # add \ after and due to line break
        if book.get('author').casefold()==book_author.casefold() and \
            book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
        return books_to_return


# to use body for post request we need to import BODY
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# update or change the book
@app.put("/book/update_book")
async def update_book(updated_book=Body()):
    # when title matches update the book
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
            BOOKS[i]=updated_book

# delete books
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
            BOOKS.pop(i)
            break

# assignment solution - using path params
@app.get("/books/fetch_books_by_author_path/{author_name}")
# http://127.0.0.1:8000/books/fetch_books_by_author_path/author%20six
async def fetch_books_by_author_path(author_name:str):
    books_to_return = []
    for book in BOOKS:
        # add \ after and due to line break
        if book.get('author').casefold() == author_name.casefold():
            books_to_return.append(book)
    return books_to_return

# assignment solution - using query params
# this will cause issue because this name will clash with already existing dynamic params
#  solution is to move up or change the route path
#  order is important in fast api
@app.get("/books/fetch/fetch_books_by_author_query/")
# http://127.0.0.1:8000/books/fetch/fetch_books_by_author_query/?author_name_query=author%20six
async def fetch_books_by_author_query(author_name_query:str):
    print("author_name_query",author_name_query)
    books_to_return = []
    for book in BOOKS:
        # add \ after and due to line break
        if book.get('author').casefold() == author_name_query.casefold():
            books_to_return.append(book)
    print('books_to_return',books_to_return)
    return books_to_return