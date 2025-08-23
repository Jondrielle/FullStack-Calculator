import axios from 'axios';

// Use relative path — works both locally (Docker) and deployed
const api = axios.create({
  baseURL: '/', // relative to current host
  headers: {
    "Content-Type": "application/json"
  }
});

export default api;
