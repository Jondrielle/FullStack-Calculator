import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.routes.arithmetic_routes import router

app = FastAPI()

origins = [
    "https://<your-netlify-site>.netlify.app",  # will update after Netlify deploy
]

# ✅ Add CORS middleware before including routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # for testing; later change to ["http://localhost:5173"] or your deployed Netlify URL
    allow_credentials=True,
    allow_methods=["*"],  # must include OPTIONS
    allow_headers=["*"],
)

# API routes
app.include_router(router, prefix="/api")

# Serve frontend build only if it exists
frontend_path = "frontend/dist"
if os.path.isdir(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")