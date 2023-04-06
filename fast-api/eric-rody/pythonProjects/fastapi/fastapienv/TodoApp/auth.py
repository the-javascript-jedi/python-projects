# uvicorn auth:app --reload

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
# for sql connection
from database import SessionLocal, engine
# authentication security
from fastapi.security import OAuth2PasswordRequestForm


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
# verify if the hashed password and plain password are the same
def verifyPassword(plain_password,hashed_password):
    return bcrpyt_context.verify(plain_password,hashed_password)
# verify if the hashed password and plain password are valid
def authenticate_user(username:str,password:str,db):
    user = db.query(models.Users).filter(models.Users.username==username).first()
    # if user not found return false
    if not user:
        return False
    # if password is not valid return false
    if not verifyPassword(password,user.hashed_password):
        return False
    # if valid user is found return the valid user
    return user



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

# create a token , this token will be used to make future valid requests
@app.post("/token")
async def login_for_access_token(form_data:OAuth2PasswordRequestForm=Depends(),
                                 db:Session=Depends(get_db)):
    user=authenticate_user(form_data.username,form_data.password,db)
    print("user",user)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return "User Validated"
