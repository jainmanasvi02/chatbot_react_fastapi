from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql+asyncpg://postgres:sylus@localhost:5432/chatbot_db"
DATABASE_URL = "postgresql+asyncpg://chatbot_db_ath7_user:IRNOcuA6Zy3WnmHfr3LQnQH6p0voiQzC@dpg-d1gisvumcj7s73cr6iug-a.singapore-postgres.render.com/chatbot_db_ath7"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
