# uvicorn main: app - -reload
from fastapi import FastAPI, Depends,HTTPException
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

# create new function to get db
def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def read_all(db: Session=Depends(get_db)):
    return db.query(models.Todos).all()

@app.get("/todo/{todo_id}")
async def read_todo(todo_id:int,db:Session=Depends(get_db)):
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    # if not
    raise http_exception()

def http_exception():
    return HTTPException(status_code=404,detail="Todo not found")
