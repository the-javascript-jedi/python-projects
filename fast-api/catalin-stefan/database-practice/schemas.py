from pydantic import BaseModel

# data that comes from the user
class UserBase(BaseModel):
    username:str
    email:str
    password:str

# data that system sends back to the user
class UserDisplay(BaseModel):
    username:str
    email:str
    # orm_mode=True - allows system to return database data our format that we have provided here
    # without the orm_mode=True we will get an error saying that we cannot convert one data type to another
    class Config():
        orm_mode=True
