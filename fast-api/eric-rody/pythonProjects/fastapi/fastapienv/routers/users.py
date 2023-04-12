import sys
sys.path.append("...")

from fastapi import Depends, APIRouter
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user,get_user_exception,verifyPassword,get_password_hash

router=APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404:{"description":"Not Found"}}
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

# pydantic class object for verification
class UserVerification(BaseModel):
    username:str
    password:str
    new_password:str

# API calls
@router.get("/")
async def read_all(db:Session=Depends(get_db)):
    return db.query(models.Users).all()

# get the user by path values
@router.get("/user/{user_id}")
async def user_by_path(user_id:int,db:Session=Depends(get_db)):
    user_model=db.query(models.Users).filter(models.Users.id==user_id).first()
    if user_model is not None:
        return user_model
    return 'Invalid user_id'

# get the user by query params
@router.get("/user/")
async def user_by_query(user_id:int,db:Session=Depends(get_db)):
    user_model=db.query(models.Users).filter(models.Users.id==user_id).first()
    if user_model is not None:
        return user_model
    return 'Invalid user_id'

# change user password if user is authenticated
@router.put("/user/password")
async def user_password_change(user_verification:UserVerification,user:dict=Depends(get_current_user),db:Session=Depends(get_db)):
    if user is None:
        raise get_user_exception()

    user_model=db.query(models.Users).filter(models.Users.id==user.get('id')).first()

    if user_model is not None:
        if user_verification.username==user_model.username and verifyPassword(
            user_verification.password,
            user_model.hashed_password):

            user_model.hashed_password=get_password_hash(user_verification.new_password)
            db.add(user_model)
            db.commit()
            return 'successful'
    return 'Invalid user or request'

@router.delete("/user")
async def delete_user(user:dict=Depends(get_current_user),db:Session=Depends(get_db)):
    if user is None:
        raise get_user_exception()
    user_model=db.query(models.Users).filter(models.Users.id==user.get('id')).first()

    if user_model is None:
        return "Invalid user or request"
    db.query(models.Users).filter(models.Users.id==user.get("id")).delete()
    db.commit()
    return "Delete Successful"