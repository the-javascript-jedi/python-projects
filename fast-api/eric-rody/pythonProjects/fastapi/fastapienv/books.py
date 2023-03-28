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
@app.get("/books/mybook")
async def read_all_books():
    return {'book_title':'My favourite book!'}

# Dynamic Param
@app.get("/books/{book_title}")
# the dynamic param will be changed to a string eg number 1 becomes string "1"
async def read_all_books(book_title:str):
    for book in BOOKS:
        # casefold makes string lowercase
        if book.get('title').casefold()==book_title.casefold():
            return book
