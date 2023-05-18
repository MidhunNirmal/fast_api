from pydantic import BaseModel
from typing import List,Union


class blogbase(BaseModel):
    tittle:str
    body:str


class blog(blogbase):
    tittle:str
    body:str
    class Config():
        orm_mode = True


class usersschema(BaseModel):
    username:str
    email:str
    password:str


class showuser(BaseModel):
    name:str
    email:str
    #blogss: list[blogbase]
    class Config():
        orm_mode = True
class showuser1(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True
    

class showid(BaseModel):
    tittle:str
    body:str
    creator:showuser
    class Config():
        orm_mode = True

class login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email:Union[str, None] = None
