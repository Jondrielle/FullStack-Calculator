from fastapi import FastAPI
from backend.routes.arithmetic_routes import router  # import router from your routes file

app = FastAPI()

app.include_router(router)
