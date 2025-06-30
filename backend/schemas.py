from pydantic import BaseModel,EmailStr

#from datetime import datetime

#class MessageCreate(BaseModel):
#    content: str

#class MessageResponse(BaseModel):
#    id: int
#    sender: str
#    content: str
#    timestamp: datetime

#    class Config:
#        orm_mode = True

class MessageCreate(BaseModel):
    email: EmailStr
    content: str

class MessageResponse(BaseModel):
    user_message: str
    bot_response: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
