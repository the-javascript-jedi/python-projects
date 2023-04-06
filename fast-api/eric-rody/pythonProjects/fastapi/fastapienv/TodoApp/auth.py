# uvicorn auth:app --reload

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
# for sql connection
from database import SessionLocal, engine

class CreateUser(BaseModel):
    username:str
    email:Optional[str]
    first_name:str
    last_name:str
    password:str

bcrpyt_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
# sql connection
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):
    return bcrpyt_context.hash(password)

@app.post("/create/user")
async def create_new_user(create_user:CreateUser,db:Session=Depends(get_db)):
    create_user_model=models.Users()
    create_user_model.email=create_user.email
    create_user_model.username=create_user.username
    create_user_model.first_name=create_user.first_name
    create_user_model.last_name=create_user.last_name
    # hash the password using bcrypt
    hash_password=get_password_hash(create_user.password)

    create_user_model.hashed_password = hash_password
    create_user_model.is_active=True

    db.add(create_user_model)
    db.commit()