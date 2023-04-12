import sys
# since router needs to access other files in directory we use this hack
sys.path.append("..")
from typing import Optional
from fastapi import Depends, APIRouter
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user,get_user_exception,verifyPassword,get_password_hash

router=APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404:{"description":"Not found"}}
)

# setup db
# create new function to get db
def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

# pydantic class object for verification
class Address(BaseModel):
    address1:str
    address2:Optional[str]
    city:str
    state:str
    country:str
    postalcode:str

# since we have created tables using alembic allready ths below code is not necessary for now
# models.Base.metadata.create_all(bind=engine)