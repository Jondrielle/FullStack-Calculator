# ================================
# Stage 1 - Build the Vue frontend
# ================================
FROM node:18 AS frontend-builder

# Set working dir for frontend
WORKDIR /frontend

# Copy only package.json and lockfile first (for caching npm install)
COPY frontend/package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the frontend code
COPY frontend/ .

# Build Vue app
RUN npm run build


# ================================
# Stage 2 - Backend (FastAPI)
# ================================
FROM python:3.11-slim

# Set working dir for backend
WORKDIR /app

# Copy requirements first (cache pip install)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Copy Vue dist from first stage into backend container
COPY --from=frontend-builder /frontend/dist ./frontend/dist

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
