import sys
import os
import pytest

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

@pytest.mark.parametrize(
    "expr, expected",
    [
        ("9 + -3", 6),
        ("9 + 21 ^ 4", 194490),
        ("-3.5 + 4 * -2.1 / 7", -4.7),  # You can add more expressions here
        ("5 / 0", "Division by zero is not allowed")
    ]
)
def test_evaluate_expression_route(expr, expected):
    response = client.post("/api/calculate", json= {"expr": expr})
    print(response.json())
    assert response.json() == {"result": expected}

