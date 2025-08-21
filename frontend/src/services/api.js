import axios from 'axios'

// Use environment variable (set in Netlify), fallback to localhost for dev
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});

export default api
