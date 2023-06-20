from email.policy import HTTP

from fastapi import FastAPI, HTTPException

from exceptions import StoryException
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from db import models
# import the engine from the created db file
from db.database import engine
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse

app=FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)

@app.get("/hello")
def index():
    return {"message":"Hello World!"}

@app.exception_handler(StoryException)
def story_exception_handler(request:Request,exc:StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail":exc.name}
    )
# this will handle all exceptions globally, so better to comment it out so it wont interfere with future lectures
@app.exception_handler(HTTPException)
def custom_handler(request:Request,exc:StoryException):
    return PlainTextResponse(str(exc),status_code=400)

models.Base.metadata.create_all(engine)