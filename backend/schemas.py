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
    username: str
    content: str

class MessageResponse(BaseModel):
    user_message: str
    bot_response: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
