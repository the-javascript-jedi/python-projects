from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# @app.get('/blog/all')
# # the request should contain the same name (i.e page,page_size)
# # http://127.0.0.1:8000/blog/all?page=1&page_size=11
# def get_blogs(page = 1, page_size: Optional[int] = None):
#   return {'message': f'All {page_size} blogs on page {page}'}

# combination of query params and path params
@app.get('blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}
