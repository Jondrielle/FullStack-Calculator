import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.routes.arithmetic_routes import router

app = FastAPI()

origins = os.getenv("FRONTEND_URLS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

frontend_path = os.getenv("FRONTEND_DIST", "frontend/dist")  # <- must match Docker ENV
if os.path.isdir(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

print("Frontend path exists?", os.path.isdir(frontend_path))
@app.get("/")
async def root():
    return {"message": "Hello Calculator App"}
