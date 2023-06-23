# uvicorn main:app --port 8001  --reload
#  http://127.0.0.1:8001/docs
from typing import Optional
from fastapi import FastAPI, Request
from router import blog_get, blog_post, user, article, product
from auth import authentication
from db.database import engine
from db import models
from exceptions import StoryException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
  return JSONResponse(
    status_code=418,
    content={'detail': exc.name}
  )

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#   return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)

origins = [
  'http://localhost:3000',
  'http://127.0.0.1:5500',
  'http://localhost:4200'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ['*']
)