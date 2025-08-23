import axios from 'axios'

// Choose base URL based on environment
const baseURL =
  import.meta.env.MODE === 'development'
    ? 'http://localhost:8000'           // local FastAPI backend
    : 'https://fullstack-calculator.onrender.com'  // deployed backend

const api = axios.create({
  baseURL: baseURL,
  headers: {
    "Content-Type": "application/json"
  }
})

export default api
