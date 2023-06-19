from fastapi import APIRouter,Depends
from typing import List
from db import db_user
from db.database import get_db
from schemas import UserBase,UserDisplay
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/user",
    tags=['user']
)

# Create User
@router.post("/",response_model=UserDisplay)
# using dependency injection we need to get the db
def create_user(request:UserBase,db:Session=Depends(get_db)):
    # since we give the response_model=UserDisplay,  the system automatically converts from one to the other
    # because we have specified the mode here this allows the system to automatically do the conversion. because
    # we have specified orm_mode = True
    return db_user.create_user(db,request)

# Read All Users
@router.get("/",response_model=List[UserDisplay])
def get_all_users(db:Session=Depends(get_db)):
    return db_user.get_all_users(db)

# Read One User
@router.get("/{id}",response_model=UserDisplay)
def get_user(id:int,db:Session=Depends(get_db)):
    return db_user.get_user(db,id)

# Update user
@router.post("/{id}/update")
def update_user(id:int,request:UserBase,db:Session=Depends(get_db)):
    return db_user.update_user(db,id,request)
