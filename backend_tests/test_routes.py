import sys
import os

# Add root folder to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now imports will work
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_connect_to_root():
    response = client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Calculator App"}

def test_add_route():
    response = client.post("/add", json={"x":0.0,"y":1293.0})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"result": 1293.0 }

def test_sub_route():
    response = client.post("/sub", json={"x":-2.0,"y":18.0})
    print(response.json())
    assert response.json() == {"result": -20.0}

def test_multiply_route():
    response = client.post("/multiply", json={"x":9.0,"y":0.0})
    print(response.json())
    assert response.json() == {"result": 0.0}

#def test_divide_route():
 #   response = client.post("/divide")
  #  print(response.json())

def test_exponent_route():
    response = client.post("/exponent", json={"x":9.0,"y":0.0})
    print(response.json())
    assert response.json() == {"result": 1.0}