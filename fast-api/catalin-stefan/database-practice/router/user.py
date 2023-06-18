from fastapi import APIRouter,Depends

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
