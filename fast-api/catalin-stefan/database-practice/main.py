from fastapi import FastAPI
from router import blog_get,blog_post
from db import models
# import the engine from the created db file
from db.database import engine

app=FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get("/hello")
def index():
    return {"message":"Hello World!"}

models.Base.metadata.create_all(engine)