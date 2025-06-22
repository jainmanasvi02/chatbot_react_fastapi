from sqlalchemy.ext.asyncio import create_async_engine
from .models import Base  
import asyncio

DATABASE_URL = "postgresql+asyncpg://postgres:sylus@localhost:5433/chatbot_db"

engine = create_async_engine(DATABASE_URL, echo=True)

async def reset_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(reset_db())
