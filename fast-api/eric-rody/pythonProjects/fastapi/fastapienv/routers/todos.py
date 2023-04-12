# uvicorn main:app --reload
import sys
# since router needs to access other files in directory we use this hack
sys.path.append("..")
from fastapi import Depends,HTTPException,APIRouter
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel,Field
from typing import Optional
# from same directory get the methods in .auth
from .auth import get_current_user,get_user_exception
# import router file

# router without prefix
# router=APIRouter()

# router with prefix
router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404:{"description":"Not found"}}
)

models.Base.metadata.create_all(bind=engine)

# create new function to get db
def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

# create a class for making POST request
class Todo(BaseModel):
    title:str
    description:Optional[str]
    priority:int=Field(gt=0,lt=6,description="The priority must be between 1 - 5")
    complete:bool
# GET all
@router.get("/")
async def read_all(db: Session=Depends(get_db)):
    return db.query(models.Todos).all()

# GET todods of the user
@router.get("/todos/user")
async def read_all_by_user(user:dict=Depends(get_current_user),db:Session=Depends(get_db)):
    if user is None:
        raise get_user_exception()
    # todos= db.query(models.Todos).filter(models.Todos.owner_id==user.get("id")).all()
    # the .filter(models.Todos.owner_id==user.get("id") is not working
    todos= db.query(models.Todos).all()


    print('todos',todos)
    return todos

# GET by id
@router.get("/{todo_id}")
async def read_todo(todo_id:int,user:dict=Depends(get_current_user),db:Session=Depends(get_db)):
    # if user is none raise an exception
    if user is None:
        raise get_user_exception()
    # todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).filter(models.Todos.owner_id==user.get("id")).first()
    # the .filter(models.Todos.owner_id==user.get("id") is not working
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()

    if todo_model is not None:
        return todo_model
    # if not
    raise http_exception()
#  POST - Create Request
@router.post("/")
async def create_todo(todo:Todo,
                      user:dict=Depends(get_current_user),
                      db:Session=Depends(get_db)):
    todo_model=models.Todos()
    todo_model.title=todo.title
    todo_model.description=todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")

    db.add(todo_model)
    db.commit()

    return{
        'status':201,
        'transaction':'Successful'
    }

@router.put("/{todo_id}")
async def update_todo(todo_id:int,
                      todo:Todo,
                      user:dict=Depends(get_current_user),
                      db:Session=Depends(get_db)):
    # if user is not present raise an exception
    if user is None:
        raise get_user_exception()

    # todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).filter(models.Todos.owner_id==user.get("id")).first()
    # the .filter(models.Todos.owner_id==user.get("id") is not working
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()

    if todo_model is None:
        raise http_exception()
    # set values from request
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return {
        'status': 200,
        'transaction': 'Successful'
    }

@router.delete("/{todo_id}")
async def delete_todo(todo_id:int,
                      user:dict=Depends(get_current_user),
                      db:Session=Depends(get_db)):

    # raise exception if user is none
    if user is None:
        raise get_user_exception()
    # todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id==todo_id).first()
    # the .filter(models.Todos.owner_id==user.get("id") is not working
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is None:
        raise http_exception()

    db.query(models.Todos).filter(models.Todos.id==todo_id).delete()

    db.commit()

    return successful_response(200)


# success helper function
def successful_response(status_code:int):
    return {
        'status': status_code,
        'transaction': 'Succesful'
    }

# exception helper function
def http_exception():
    return HTTPException(status_code=404,detail="Todo not found")