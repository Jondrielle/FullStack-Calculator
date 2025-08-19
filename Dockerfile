FROM python:3.11-slim

WORKDIR /app

# Copy backend requirements
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the built frontend
COPY frontend/dist ./frontend/dist

# Copy backend source
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
