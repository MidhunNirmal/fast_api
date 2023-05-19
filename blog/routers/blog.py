from fastapi import APIRouter
from blog import models,schemas
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from blog.databse import engine,SessionLocal,get_db
from blog import oaut2
# from .schemas import blog
# from .models import Blog
from blog.databse import engine,SessionLocal
from passlib.context import CryptContext

router = APIRouter(
    tags=['blogs']
)

@router.get('/blog',response_model=list[schemas.showid])
def getall(db : Session = Depends(get_db),current_user: schemas.usersschema= Depends(oaut2.get_current_user)):
    myblogs = db.query(models.blog).all() 
    return myblogs 

@router.post("/blog",status_code=status.HTTP_201_CREATED,)
def create(request:schemas.blogbase, db : Session = Depends(get_db),current_user: schemas.usersschema= Depends(oaut2.get_current_user)):
    # return "create"
    new_blog = models.blog(tittle = request.tittle,body = request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog



@router.get('/blog/{id}',response_model=schemas.showid)
def getid(id,response:Response,db : Session = Depends(get_db),current_user: schemas.usersschema= Depends(oaut2.get_current_user)):
    theblogs = db.query(models.blog).filter(models.blog.id==id).first()
    if not theblogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"details":f"the blog with id +{id}+ is not found"})
        # response.status_code = status.HTTP_404_NOT_FOUND
        
    return theblogs  


@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.blogbase, db: Session = Depends(get_db),current_user: schemas.usersschema= Depends(oaut2.get_current_user)):
    update_blog = db.query(models.blog).filter(models.blog.id == id).first()

    if not update_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    update_blog.tittle = request.title
    update_blog.body = request.body
    # update_blog.update(request)
    db.commit()
    return "Updated"


@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deleteblog(id,db : Session = Depends(get_db),current_user: schemas.usersschema= Depends(oaut2.get_current_user)): 
    db.query(models.blog).filter(models.blog.id==id).delete(synchronize_session=False)
    db.commit()
    return "done"


