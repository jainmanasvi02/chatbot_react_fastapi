from models import User
from utils import hash_password, verify_password
from sqlalchemy.future import select

async def create_user(db, email: str, password: str):
    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_email(db, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()
