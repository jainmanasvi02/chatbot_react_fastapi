import axios from "axios";

export function logErrorToServer(error, info = "") {
  axios.post("http://127.0.0.1:8000/log", {
    error: error.toString(),
    info,
    location: window.location.href,
  }).catch(err => {
    console.error("Failed to send error log:", err);
  });
}
