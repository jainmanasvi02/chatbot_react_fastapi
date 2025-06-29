from pydantic import BaseModel
from datetime import datetime

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
    email: str
    content: str

class MessageResponse(BaseModel):
    user_message: str
    bot_response: str

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
