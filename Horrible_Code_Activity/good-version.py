# This is our good calc
# Calc is slang for those who are new here


# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_numbers():
    """Prompt the user for two numbers and return them as floats."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b
