from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine, Base
from . import schemas, crud
from .util import verify_password
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/signup", response_model=schemas.TokenResponse)
async def signup(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    existing = await crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await crud.create_user(db, user.email, user.password)
    return {"access_token": new_user.email, "token_type": "bearer"}

@app.post("/signin", response_model=schemas.TokenResponse)
async def signin(user: schemas.UserLogin, db: AsyncSession = Depends(get_db)):
    existing = await crud.get_user_by_email(db, user.email)
    if not existing or not verify_password(user.password, existing.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": existing.email, "token_type": "bearer"}
