from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal, engine, Base
#from . import models, schemas, crud, llm_provider
import models, schemas, crud, llm_provider
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.future import select
from fastapi.responses import JSONResponse
#from backend.logger import logger
from logger import logger
import traceback
from pydantic import BaseModel, EmailStr


app = FastAPI()

#forcing redploy

#origins = ["https://localhost:3000", https://frontend-eight-black-76.vercel.app]
# Temporarily allowing all origins for development, above origin is not working
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    email: EmailStr
    content: str
    
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
    user = await crud.get_user_by_email(db, message.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Save user message
    user_msg = await crud.create_user_message(db, user.email, message.content)
   

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
    db_user = await crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    await crud.create_user(db, user)
    return {"message": "User created successfully"}

# SIGNIN
@app.post("/signin")
async def signin(user: schemas.UserLogin, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, user.email)
    print(f"db_user: {db_user}")
    print("entered password:", user.password)
    if not db_user or db_user.password != user.password:
        print("Login failed")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    print("Login successfull")
    return {"message": "Login successful", "username": db_user.email}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    stack_trace = traceback.format_exc()
    logger.error(f"Unhandled error at {request.url}\n{stack_trace}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Please try again later."}
    )


# GET CHAT HISTORY
@app.get("/history/{email}")
async def get_history(email: str, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    result = await db.execute(
        select(models.UserMessage).where(models.UserMessage.user_id == user.id)
    )
    user_messages = result.scalars().all()

    result = await db.execute(
        select(models.BotResponse).where(models.BotResponse.user_id == user.id)
    )
    bot_messages = result.scalars().all()

    return {
        "user_messages": [msg.content for msg in user_messages],
        "bot_responses": [msg.content for msg in bot_messages]
    }


@app.post("/log")
def receive_log(data: dict):
    print("Frontend log:", data)
    return {"status": "received"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
