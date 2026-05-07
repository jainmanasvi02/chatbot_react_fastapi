# AI Chatbot Application

A full-stack AI-powered chatbot application built using React.js, FastAPI and PostgreSQL.  
The project provides fast response times (1–3 seconds), scalable backend architecture, secure authentication and real-time conversational interaction.

---

## Features

-  Fast chatbot responses (1–3s latency)
-  AI-powered conversational interface
-  User authentication and authorization
-  PostgreSQL database integration
-  RESTful APIs using FastAPI
-  Responsive frontend with React.js
-  Scalable backend architecture
-  Chat history management
-  CORS-enabled frontend/backend communication


---

## Tech Stack

### Frontend
- React.js
- Axios
- HTML/CSS 

### Backend
- FastAPI
- Python
- Uvicorn

### Database
- PostgreSQL

### AI/LLM Integration
- Gemini API 

### Additional Tools
JWT Authentication
SQLAlchemy
Pydantic
---

## Project Structure

project-root/
│
├── frontend/                 # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/                  # FastAPI backend
│   ├── __init__.py
│   ├── crud.py
│   ├── models.py
│   ├── database
│   ├── requirements.txt
│   ├── main.py
|   ├── logger.py
|   ├── llm_provider.py
|   ├── schemas.py
|   └── init_db.py
|
│
|── auth_service/                  # Authorization
 ├── crud.py
│   ├── models.py
│   ├── database
│   ├── requirements.txt
│   ├── main.py
|   ├── crud.py
|   ├── schemas.py
|   └── util.py
|
|
├── README.md

Installation & Setup
1. Clone the Repository
  git clone https://github.com/jainmanasvi02/chatbot_react_fastapi.git
  cd chatbot_react_fastapi

2. Backend Setup (FastAPI)
  Create Virtual Environment
    a. Windows
        python -m venv venv
        venv\Scripts\activate
    b. Linux/Mac
        python3 -m venv venv
        source venv/bin/activate

 Configure Environment Variables
 Create a .env file inside the backend folder:
 
  DATABASE_URL=postgresql://username:password@localhost:5432/chatbot_db
  SECRET_KEY=your_secret_key
  API_KEY=your_api_key
   
 Run Backend Server
    uvicorn main:app --reload       
    Backend will start at: http://127.0.0.1:8000
    Swagger API Docs: http://127.0.0.1:8000/docs

3. Frontend Setup (React.js)
  Navigate to Frontend
      cd frontend
  Install Dependencies
      npm install
  Start React Application
      npm start
  Frontend runs at:
      http://localhost:3000

4. PostgreSQL Setup
    Install PostgreSQL
    Open PostgreSQL shell
    Create database:
        CREATE DATABASE chatbot_db;
    Update credentials inside .env

Performance
- Average response time: 1–3 seconds
- Optimized API communication
- Efficient database querying
- Scalable backend design
- Supports concurrent users efficiently

Security Features
- JWT Authentication
- Password hashing
- Protected API routes
- Environment variable security
- Secure database handling

-> Testing
1. Backend Testing
      pytest
2. Frontend Testing
      npm test

Author:
Manasvi Jain
