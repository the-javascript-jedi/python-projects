from typing import List

import xlsxwriter
from starlette.responses import StreamingResponse

from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from auth.oauth2 import get_current_user
from io import BytesIO

router = APIRouter(
  prefix='/user',
  tags=['user']
)

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
  return db_user.create_user(db, request)

# Read all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db),current_user:UserBase = Depends(get_current_user)):
  return db_user.get_all_users(db)

# Read one user
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db),current_user:UserBase = Depends(get_current_user)):
  return db_user.get_user(db, id)

# Update user
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db),current_user:UserBase = Depends(get_current_user)):
  return db_user.update_user(db, id, request)

# Delete user
@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db),current_user:UserBase = Depends(get_current_user)):
  return db_user.delete_user(db, id)

@router.get("/payments/xlsx", response_description='xlsx')
async def payments():
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'ISBN')
    worksheet.write(0, 1, 'Name')
    worksheet.write(0, 2, 'Takedown date')
    worksheet.write(0, 3, 'Last updated')
    worksheet.write(1, 0, 'second isbn')
    worksheet.write(1, 1, 'second Name')
    worksheet.write(1, 2, 'second Takedown date')
    worksheet.write(1, 3, 'second Last updated')
    workbook.close()
    output.seek(0)

    headers = {
        'Content-Disposition': 'attachment; filename="filename.xlsx"'
    }
    return StreamingResponse(output, headers=headers)