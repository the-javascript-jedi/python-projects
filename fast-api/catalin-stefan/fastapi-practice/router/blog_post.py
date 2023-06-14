from typing import Optional,List,Dict
from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)
# Image class to be used as a type in BlogModel class
class Image(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel):
  title: str
  content: str
  nb_comments: int
  published: Optional[bool]
  tags:List[str]=[]
  metadata:Dict[str,str]={'key1':'val1'}
  image:Optional[Image]=None

@router.post('/new/{id}')
def create_blog(blog: BaseModel, id: int, version: int = 1):
  return {
    'id': id,
    'data': blog,
    'version': version
    }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int,
        comment_id: int = Query(None,
            title='Id of the comment',
            description='Some description for comment_id',
            alias='commentId',
            deprecated=True
        ),
        content: str = Body(...,
            min_length=10,
            max_length=50,
            # Lowercase or spaces
            regex='^[a-z\s]*$'
        ),
        v:Optional[List[str]]=Query(None)
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content,
        'version':v
    }