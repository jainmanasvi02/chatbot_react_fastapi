This is the **backend service** for the Chatbot App built using **FastAPI**. It handles user authentication, message processing, database operations, and communicates with an LLM (e.g., Gemini or OpenAI) to generate responses.


## Features

- User Signup and Signin APIs
- Secure password hashing 
- Chat API integrated with LLM (Gemini)
- PostgreSQL database integration using SQLAlchemy
- Modular and clean project structure



## Folder Structure

backend/
├── main.py # FastAPI entry point
├── database.py # DB connection and setup
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
├── crud.py # DB operations
├── llm_provider.py/ # LLM integration logic
├── init_db.py # initialize the database
├── README.md # This file


## Setup Instructions

### 1. Create and activate virtual environment

bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
### 2. Install dependencies
bash
pip install -r requirements.txt

### 3. Set up environment variables 
DATABASE_URL=postgresql://username:password@localhost/dbname
GEMINI_API_KEY=your-api-key

### 4. Run the application
bash
uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs to access the Swagger API documentation.


## 🛠 Tech Stack
Python
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
Passlib
Gemini API

## Author
Made by Manasvi Jain