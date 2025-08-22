import axios from 'axios'

// Use environment variable (set in Netlify), fallback to localhost for dev
const api = axios.create({
  baseURL: "https://fullstack-calculator.onrender.com" || "http://localhost:8000",
});


export default api
