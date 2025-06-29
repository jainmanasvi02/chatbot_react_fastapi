import axios from "axios";
const BASE_URL = process.env.REACT_APP_AUTH_URL;


//export function logErrorToServer(error, info = "") {
 // axios.post("http://127.0.0.1:8000/log", {
 //   error: error.toString(),
 //   info,
 //   location: window.location.href,
 // }).catch(err => {
 //   console.error("Failed to send error log:", err);
 // });
//}


export async function logErrorToServer(error, context = "") {
  try {
    await fetch(`${BASE_URL}/log`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ error: error.toString(), context })
    });
  } catch (err) {
    console.error("Failed to send error log:", err);
  }
}