# Simple Web Calculator 
A lightweight, beginner-friendly web-based calculator built with **Python** and **FastAPI**. It allows users to perform basic arithmetic operations through a clean and simple web interface. 

## Project Structure 
<details>

```
calculator/
├── backend/
│   ├── logic/
│   │   └── calculator.py
│   ├── models/
│   │   └── arithmetic_models.py
│   ├── routes/
│   │   └── arithmetic_routes.py
│   ├── __init__.py
│   └── main.py
├── backend_test/
│   ├── test_calculator_logic.py
│   ├── test_routs.py
├── frontend/
│   ├── src/
│   │   ├── components
│   │   │   └── Calculator.vue
│   │   ├── services
│   │   │   └── api.js
│   │   ├── App.vue
│   │   └── main.js
│   ├── public/
│   └── package.json
├── Dockerfile
├── .dockerignore
├── main.py
├── .gitignore
├── README.md
└── requirements.txt
  
```
</details> 

## Features 
- Basic arithmetic: **addition**, **subtraction**, **multiplication**, **divison**, **power**
- Operation chaining
- Responsive Web based interface
- Backend API built with FastAPI
- CI/CD integration with Github Actions
- CORS-enabled for frontend-backend communication
- Dockerized for consistent development and production environments
- Frontend deployed on Netlify, backend deployed on Render
- CI/CD integration via GitHub Actions

## Technologies Used
- Backend: Python, FastAPI, Uvicorn
- Frontend: Vue, Vite, Axios
- Deployment: Docker, Render, Netlify
- Version Control: Git, GitHub

## Getting Started
#### Prerequisites: 
- Python 3.8+
- Git
- Node.js and npm 
- Docker (optional, for containerized setup but recommended for easier setup)

## Development 
#### Option 1: Without Docker (Local Development):
1. Clone the repo
   ```
     git clone \n
     cd Calculator 
   ```
2. Backend
    ```
     cd backend
     pip install -r requirements.txt
     uvicorn main:app --reload 
   ```
3. Frontend
   ```
     cd frontend
     npm install
     npm run dev
   ```
4. Open http://localhost:5173 in your browser to use the calculator

#### Option 2: With Docker (Recommended): 
1. Build Docker Image
  ` docker build -t calculator-app .`
2. Run the container
  ` docker run -p 8000:8000 calculator-app`
3. Visit http://localhost:8000 to use the calculator
   - Docker handles both backend and frontend automatically, serving the built frontend through FastAPI

## Deployment
#### Option 1: Free-tier Render + Netlify (without Docker):
##### - Backend: Deploy FastAPI app to Render:
- Build command: pip install -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 8000
- Free-tier limitations: auto-sleep, limited CPU and RAM

##### - Frontend: Deploy Vite project to Netlify:
- Build command: npm run build
- Publish directory: dist
- Free-tier limitations: slower builds, max bandwidth limits

- Upddate .env or origins in backend to allow requests from your deployed Netlify URL

#### Option 2: Docker Deployment (Render or AWS):
1. Build Docker image contraining both frontend and backend 
2. Push to Docker registry(optional) and deploy on Render or AWS
3. Docker automatically handles installing dependencies and serving static files
4. Free-tier limitations depend on the hosting provider (e.g., Render free-tier has auto-sleep, AWS free-tier has 750h/month EC2)
   ```
   docker build -t calculator-app .
   docker run -p 8000:8000 calculator-app 
   ```
5. Access your live app at the URL provided by your host 

#### Backend (Render):
1. Push your repository to GitHub
2. Connect Render to your GitHub repo
3. Use Docker as the environment
4. Render automatically builds and deploys your backend

#### Frontend (Netlify):
1. Push your frontend code to GitHub
2. Connect Netlify to your GitHub repo
3. Set the build command: npm run build
4. Set the publish directory: dist

#### After deployment:
- Your frontend is live on Netlify
- Your backend API is live on Render
- CORS and environment variables ensure proper communication

## Using the Calculator 
1. Open the frontend in your browser
2. Enter numbers and select an operation (supports chaining operations)
3. Click "=" to get results
4. The frontend communicates with the backend API for calculations via Axios 

## CI/CD Integration
- Github Actions can automatically build and push Docker images or deploy to Render/Netlify
- Ensure environment variables are configured in CI/CD settings

## Optional: Using .env file
#### Frontend/.env
```
VITE_API_URL=https://your-render-backend-url
```
- In api.js you can use this
```
import axios from "axios";

const baseURL = import.meta.env.VITE_API_URL;
export const api = axios.create{{baseURL}};
```
#### Backend/.env
```
FRONTEND_URLS=https://your-netlify-frontend-url,http://localhost:5173
FRONTEND_DIST=frontend/dist
```
- Save and redeploy after setting variables
Note: .env files are **not included** in the repo for security. You need to set the env variables manually when deploying on Netlify and Render 




