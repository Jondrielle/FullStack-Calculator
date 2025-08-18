import sys
import os
import pytest

# Add root folder to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.logic.calculator import add, sub, multiply, divide, power, evaluate_expression

def test_add():
    assert add(4,3) == 7

def test_sub():
    assert sub(3,-12321) == 12324

def test_multiply():
    assert multiply(2,1) == 2

def test_divide():
    result = divide(3,124) 
    assert round(result,4) == 0.0242

def test_power():
    assert power(2,3) == 8

def test_evaluate_expression():
    assert evaluate_expression("-3.5 + 4 * -2.1 / 7") == -4.7

def test_division_by_zero():
   with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
        divide(4, 0)
