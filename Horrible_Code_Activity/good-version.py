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
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

# Main program
def main():
    print("Simple Calculator")
    print("Choose an operation: +, -, *, /")
    choice = input("Enter operation: ")

    a, b = get_numbers()

    if choice == "+":
        print("Result:", add(a, b))
    elif choice == "-":
        print("Result:", subtract(a, b))
    elif choice == "*":
        print("Result:", multiply(a, b))
    elif choice == "/":
        print("Result:", divide(a, b))
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    main()