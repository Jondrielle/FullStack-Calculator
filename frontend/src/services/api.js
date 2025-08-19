import axios from 'axios'

const api = axios.create({
  baseURL: 'https://my-calculator.onrender.com/api',  // your FastAPI backend URL
})

export default api
