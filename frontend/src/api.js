import axios from 'axios';
import { logErrorToServer } from "./logger";

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000', 
});

instance.interceptors.response.use(
  response => response,
  error => {
    logErrorToServer(error, "Axios response error");
    return Promise.reject(error);
  }
);

export default instance;
