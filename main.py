import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from backend.routes.arithmetic_routes import router

# load variables from .env
load_dotenv()

app = FastAPI()

# get allowed origins from env (split into list by commas)
origins = os.getenv("FRONTEND_URLS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(router, prefix="/api")

# Serve frontend build only if it exists
frontend_path = "frontend/dist"

if os.path.isdir(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
    
@app.get("/")
async def root():
    return {"message": "Hello Calculator App"}
