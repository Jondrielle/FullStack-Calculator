import re

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

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y

def power(x,y): 
    return float(x) ** float(y)


def evaluate_expression(expr):
    expr = expr.replace(' ', '')

    # Invalid operator sequences except for negative numbers
    if re.search(r'(?<![\d)])[\+\*/]{2,}|--{2,}', expr):
        return "Invalid operation on non-numeric values"

    # Tokens: numbers (including negative) and operators
    tokens = re.findall(r'(?<!\d)-?\d+(?:\.\d+)?|[\+\-\*/\^]', expr)

    # Convert numeric tokens to float
    for i in range(len(tokens)):
        if re.match(r'-?\d+(?:\.\d+)?', str(tokens[i])):
            tokens[i] = float(tokens[i])

    def apply_operator(op_index):
        op = tokens[op_index]
        left = tokens[op_index - 1]
        right = tokens[op_index + 1]

        if op == '+':
            result = add(left, right)
        elif op == '-':
            result = subtract(left, right)
        elif op == '*':
            result = multiply(left, right)
        elif op == '/':
            result = divide(left, right)  # Will raise ZeroDivisionError if needed
        elif op == '^':
            result = power(left, right)
        else:
            raise ValueError(f"Unknown operator: {op}")


        tokens[op_index - 1:op_index + 2] = [result]


    precedence = ['^', '*', '/', '+', '-']

    try:
        for op in precedence:
            while op in tokens:
                op_index = tokens.index(op)
                apply_operator(op_index)
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except Exception:
        return "Invalid operation on non-numeric values"

    return tokens[0]