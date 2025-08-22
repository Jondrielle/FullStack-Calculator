import axios from 'axios'

// Use environment variable (set in Netlify), fallback to localhost for dev
const api = axios.create({
  baseURL: "https://fullstack-calculator.onrender.com/api",
});


export default api
