from fastapi import FastAPI
from blog import models
from blog.routers import blog,user,authentication
from blog.databse import engine


app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(blog.router) 
app.include_router(user.router) 
app.include_router(authentication.router) 

 