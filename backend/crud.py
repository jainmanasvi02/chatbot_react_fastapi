#from . import models, schemas
import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

#async def create_message(db: AsyncSession, sender: str, content: str):
#    message = models.Message(sender=sender, content=content)
##    db.add(message)
#    await db.commit()
#    await db.refresh(message)
#    return message

async def create_user_message(db: AsyncSession, email: str, content: str):
    user = await get_user_by_email(db, email)
    if user:
        msg = models.UserMessage(content=content, user_id=user.id)
        db.add(msg)
        await db.commit()
        await db.refresh(msg)
        return msg

async def create_bot_response(db: AsyncSession, content: str, user_message_id: int):
    response = models.BotResponse(content=content, user_message_id=user_message_id)
    db.add(response)
    await db.commit()
    await db.refresh(response)
    return response

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    new_user = models.User(email=user.email, password=user.password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()