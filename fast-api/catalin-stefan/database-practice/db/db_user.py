from sqlalchemy.orm import Session
from db.hash import Hash
from schemas import UserBase
from db.models import DbUser


# we need to convert the data format received in UserBase format to DBUser format to save in db
# (i.e) we will convert the received data to a data similar to schema

def create_user(db:Session,request:UserBase):
    new_user=DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    # add data to user
    db.add(new_user)
    db.commit()
    # we do the refresh to get the generated id of the user
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    return db.query(DbUser).all()

def get_user(db:Session,id:int):
    return db.query(DbUser).filter(DbUser.id==id).first()

# update user
def update_user(db:Session,id:int,request:UserBase):
    user=db.query(DbUser).filter(DbUser.id==id)
    user.update({
        DbUser.username:request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'

# delete user
def delete_user(db:Session,id:int):
    user=db.query(DbUser).filter(DbUser.id==id).first()
    db.delete(user)
    db.commit()
    return 'ok'