import axios from 'axios'

// Use environment variable (set in Netlify), fallback to localhost for dev
const api = axios.create({
  baseURL: "/api",
});

export default api
