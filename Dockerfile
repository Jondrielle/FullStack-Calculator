# ----------------------
# Stage 1: Build frontend
# ----------------------
FROM node:20 AS frontend-build
WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm install --legacy-peer-deps

COPY frontend/ ./
RUN npm run build

# ----------------------
# Stage 2: Backend
# ----------------------
FROM python:3.11-slim AS backend
WORKDIR /app

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
COPY --from=frontend-build /app/frontend/dist ./frontend/dist  

ENV FRONTEND_DIST=/app/frontend/dist  
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]