from fastapi import FastAPI
app=FastAPI()
# run the app -  uvicorn books:app --reload

BOOKS=[
    {'title': 'Title One', 'author': "Author One", "category":"science"},
    {'title': 'Title Two', 'author': "Author Two", "category": "science"},
    {'title': 'Title Three', 'author': "Author Three", "category": "history"},
    {'title': 'Title Four', 'author': "Author Four", "category": "math"},
    {'title': 'Title Five', 'author': "Author Five", "category": "math"},
    {'title': 'Title Six', 'author': "Author Six", "category": "math"},
]
# if api endpoint is repeated make sure the dynamic param is below the static param or the static value will never get executed

# Dynamic Param
# @app.get("/books/{book_title}")
# # the dynamic param will be changed to a string eg number 1 becomes string "1"
# async def read_all_books(book_title:str):
#     for book in BOOKS:
#         # casefold makes string lowercase
#         if book.get('title').casefold()==book_title.casefold():
#             return book
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
