from blog import models,schemas,tocken
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from blog.hashing import hash
from blog.databse import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException


router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    user3 = db.query(models.user).filter(models.user.email == request.username).first()
    if not user3:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"details":"invalid credential"})
    if not hash.verify(user3.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"details":"invalid password"})

    
   
    access_token = tocken.create_access_token(data={"sub": user3.email})
    return {"access_token": access_token, "token_type": "bearer"} 
