from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from .database import SessionLocal, engine, Base
from . import models, schemas, crud, llm_provider
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.future import select
from fastapi.responses import JSONResponse
from backend.logger import logger
import traceback

app = FastAPI()

origins = ["https://localhost:3000"]
# Temporarily allowing all origins for development, above origin is not working
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creating tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency of session
async def get_db():
    async with SessionLocal() as session:
        yield session

# CHAT ENDPOINT
@app.post("/chat", response_model=schemas.MessageResponse)
async def chat(message: schemas.MessageCreate, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user_by_username(db, message.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Save user message
    user_msg = await crud.create_user_message(db, user.username, message.content)
   

    # Get bot response
    try:
        response_text = await llm_provider.generate_response(message.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM call failed: {str(e)}")

    # Save bot message
    bot_msg = await crud.create_bot_response(db, response_text,  user_msg.id)

    return {"user_message": user_msg.content, "bot_response": bot_msg.content}


# SIGNUP
@app.post("/signup")
async def signup(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    await crud.create_user(db, user)
    return {"message": "User created successfully"}

# SIGNIN
@app.post("/signin")
async def signin(user: schemas.UserLogin, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_username(db, user.username)
    print(f"db_user: {db_user}")
    print("entered password:", user.password)
    if not db_user or db_user.password != user.password:
        print("Login failed")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    print("Login successfull")
    return {"message": "Login successful", "username": db_user.username}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    stack_trace = traceback.format_exc()
    logger.error(f"Unhandled error at {request.url}\n{stack_trace}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Please try again later."}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
