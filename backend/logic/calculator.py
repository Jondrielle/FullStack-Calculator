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
        return "Division by zero is not allowed"
    return x / y

def power(x,y): 
    return float(x) ** float(y)


def evaluate_expression(expr):
    # Regex to match numbers (including negative and decimals) and operators
    tokens = re.findall(r'-?\d+(?:\.\d+)?|[\+\-\*/\^]', expr)

    # Convert numeric tokens to float
    for i in range(len(tokens)):
        if re.match(r'-?\d+(?:\.\d+)?', str(tokens[i])):
            tokens[i] = float(tokens[i])

    # Handle precedence: ^ > * / > + -
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
            result = divide(left, right)
        elif op == '^':
            result = power(left, right)
        else:
            raise ValueError(f"Unknown operator: {op}")

        # Replace the three tokens (left, op, right) with the result
        tokens[op_index - 1:op_index + 2] = [result]

    # Operator precedence list
    precedence = ['^', '*', '/', '+', '-']

    # Evaluate expression based on precedence
    for op in precedence:
        while op in tokens:
            op_index = tokens.index(op)
            apply_operator(op_index)

    return tokens[0]
