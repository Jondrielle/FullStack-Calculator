def add(x,y):
    return x + y

def sub(x,y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Error: invalid input, expected numbers"
    return x - y

def multiply(x,y):
    try:
        return x * y
    except Exception as e:
        return f"Error: {e}"

def division(x,y):
    try:
        result = x / y
        return result
    except ZeroDivisionError as e:
        return f"Caught an error: {e}"

def exponent(x,y): 
    currentX = x
    while y != 1:
        currentX *= x   
        y -= 1
    return currentX


# Example usage (you can delete or change these)
print("Add:", add(4, 2))          # 6
print("Add:", add((4/2), 1))         # 3

print("Subtract:", sub(10, 3))    # 7

print("Multiply:", multiply(3, 3)) # 9
print("Multiply:", multiply(0, 1)) # 0
print("Multiply:", multiply(120, -2)) # 0

print("Divide:", division(10, 2)) # 5.0
print("Divide by 0:", division(10, 0)) # Caught an error: division by zero
