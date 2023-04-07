#  uvicorn auth:app --reload --port 9000

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
# for sql connection
from database import SessionLocal, engine
# authentication security
from fastapi.security import OAuth2PasswordRequestForm, OAuth2AuthorizationCodeBearer,OAuth2PasswordBearer
from datetime import datetime,timedelta
from jose import jwt,JWTError

# secret key for jwt
SECRET_KEY="secret_key_test"
ALGORITHM="HS256"


class CreateUser(BaseModel):
    username:str
    email:Optional[str]
    first_name:str
    last_name:str
    password:str

bcrpyt_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
# sql connection
models.Base.metadata.create_all(bind=engine)
# bearer token
oauth2_bearer=OAuth2PasswordBearer(tokenUrl="token")

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

def create_access_token(username:str,user_id:int,expires_delta:Optional[timedelta]=None):
    encode={"sub":username,"id":user_id}
    if expires_delta:
        expire=datetime.utcnow()+expires_delta
    else:
        expire=datetime.utcnow()+timedelta(minutes=15)
    encode.update({"exp":expire})
    # create encoded access token
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

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

async def get_current_user(token:str=Depends(oauth2_bearer)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        user_id:int=payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=404,detail="User not found")
            # raise get_user_exception()
        return {"username":username,"id":user_id}
    except JWTError:
        raise HTTPException(status_code=404,detail="User not found")
        # raise get_user_exception()


# create a token , this token will be used to make future valid requests
@app.post("/token")
async def login_for_access_token(form_data:OAuth2PasswordRequestForm=Depends(),
                                 db:Session=Depends(get_db)):
    user=authenticate_user(form_data.username,form_data.password,db)
    print("user",user)
    if not user:
        # raise HTTPException(status_code=404,detail="User not found")
        raise token_exception()
    # create token
    token_expires = timedelta(minutes=20)
    token=create_access_token(user.username,user.id,expires_delta=token_expires)
    # "User Validated" - return token
    return {"token":token}

# Exceptions
def get_user_exception():
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    return credentials_exception

def token_exception():
    token_exception_response=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or assword",
        headers = {"WWW-Authenticate": "Bearer"}
    )
    return token_exception_response