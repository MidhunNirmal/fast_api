from fastapi import APIRouter
from blog import models,schemas
from sqlalchemy.orm import Session
from blog.hashing import hash
from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from blog.databse import engine,SessionLocal,get_db
from passlib.context import CryptContext

router = APIRouter(tags=['user'])


@router.post('/user',response_model=schemas.showuser1)   
def create_user(request: schemas.usersschema, db: Session = Depends(get_db)):
    # hashedpass = pwd_cxt.hash(request.password)
    new_user = models.user(name=request.username, email=request.email, password=hash.hashing(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get('/getuser/{id}',response_model=schemas.showuser)
def get_user(id:int,db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"details":f"the blog with id +{id}+ is not found"})
    return user