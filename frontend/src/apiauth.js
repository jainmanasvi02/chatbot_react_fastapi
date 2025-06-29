// src/apiauth.js
import axios from 'axios';

const authInstance = axios.create({
  baseURL: 'https://chatbot-react-fastapi-1.onrender.com', // Auth backend
  headers: {
    'Content-Type': 'application/json',
  },
});

export default authInstance;
