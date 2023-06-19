# dbStep1 ... - custom steps
from pydantic import BaseModel
from typing import List
# data that comes from the user
class UserBase(BaseModel):
    username:str
    email:str
    password:str
# this is what goes inside Class UserDisplay items key
class Article(BaseModel):
    title:str
    content:str
    published:bool
    class Config():
        orm_mode=True
# dbStep1 - added type of data returned in user
# data that system sends back to the user
class UserDisplay(BaseModel):
    username:str
    email:str
    items:List[Article]=[]
    # orm_mode=True - allows system to return database data our format that we have provided here
    # without the orm_mode=True we will get an error saying that we cannot convert one data type to another
    class Config():
        orm_mode=True

# User inside ArticleDisplay
class User(BaseModel):
    id:int
    username:str
    class Config():
        orm_mode=True
# dbStep2 - define articles,
# i)what we want from user, ii)what we return to the user - including the user type we defined above
class ArticleBase(BaseModel):
    title:str
    content:str
    published: bool
    creator_id:int

# data structure to send data
class ArticleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user:User
    class Config():
        orm_mode=True

