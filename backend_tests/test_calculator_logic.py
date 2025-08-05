from backend.logic.calculator import add, sub, multiply, division, exponent

def test_add():
    assert add(4,3) == 7

def test_sub():
    assert sub(3,-12321) == 12324

def test_multiply():
    assert multiply(2,1) == 2

def test_division():
    result = division(3,124) 
    assert round(result,4) == 0.0242

def test_exponent():
    assert exponent(2,3) == 8

def test_division_by_zero():
    result = division(4, 0)
    assert isinstance(result, str)  # it should return an error message string
    assert "error" in result.lower()  # the message contains "error"

