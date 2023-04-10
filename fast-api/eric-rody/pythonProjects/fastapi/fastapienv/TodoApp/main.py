# uvicorn main:app --reload
from fastapi import FastAPI
import models
from database import engine,SessionLocal
# import router file
from routers import auth,todos

app=FastAPI()

models.Base.metadata.create_all(bind=engine)
# include the auth file
app.include_router(auth.router)
# include the router in todos
app.include_router(todos.router)

