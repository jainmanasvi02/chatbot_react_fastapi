import axios from 'axios';
import { logErrorToServer } from "./logger";

//console.log("Base URL:", process.env.REACT_APP_AUTH_URL);

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000', 
  //baseURL: process.env.REACT_APP_BACKEND_URL, 
  //baseURL: 'https://chatbot-react-fastapi-2.onrender.com',
});

instance.interceptors.response.use(
  response => response,
  error => {
    logErrorToServer(error, "Axios response error");
    console.log("api backend error-api.js");
    return Promise.reject(error);
  }
);


export default instance;
