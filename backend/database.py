from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

#from sqlalchemy import Column, Integer, String
#from .database import Base

load_dotenv()
#load_dotenv(dotenv_path="../.env")

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


#class User(Base):
#    __tablename__ = "users"
#    __table_args__ = {'extend_existing': True}
#    id = Column(Integer, primary_key=True, index=True)
#    username = Column(String, unique=True, index=True)
#    password = Column(String)
