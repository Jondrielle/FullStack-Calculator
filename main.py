import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.routes.arithmetic_routes import router

app = FastAPI()

# -------------------
# CORS configuration
# -------------------
origins = [
    "https://fullstack-calculator-app.netlify.app",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------
# API routes
# -------------------
app.include_router(router, prefix="/api")

# -------------------
# Frontend static files
# -------------------
frontend_path = "frontend/dist"
if os.path.isdir(frontend_path):
    # Mount frontend under /frontend
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

# -------------------
# JSON root endpoint
# -------------------
@app.get("/")
async def root():
    return {"message": "Hello Calculator App"}

