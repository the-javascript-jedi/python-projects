from sqlalchemy import Boolean,Column,Integer,String
from database import Base

# specify the table details
# extend the Base from databse we created
class Todos(Base):
    __tablename__="todos"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    complete=Column(Boolean,default=False)


