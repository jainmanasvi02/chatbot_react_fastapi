#from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
#from sqlalchemy.sql import func
#from .database import Base

#class Message(Base):
#    __tablename__ = "messages"

#    id = Column(Integer, primary_key=True, index=True)
#    sender = Column(String, nullable=False)  # "user" or "bot"
#    content = Column(Text, nullable=False)
#   timestamp = Column(DateTime(timezone=True), server_default=func.now())


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
#from .database import Base
from database import Base

class UserMessage(Base):
    __tablename__ = "user_messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    response = relationship("BotResponse", back_populates="user_message", uselist=False)
    user = relationship("User", back_populates="messages")


class BotResponse(Base):
    __tablename__ = "bot_responses"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user_message_id = Column(Integer, ForeignKey("user_messages.id"))
    user_message = relationship("UserMessage", back_populates="response")


class User(Base):
    __tablename__ = "users"  # Your table name

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    messages = relationship("UserMessage", back_populates="user")