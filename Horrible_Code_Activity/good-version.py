#this is our good calc
#calc is slang for those who are new here
print("Calculator")
print("Choose +, -, *, /")
op = input("Op: ")

#addition method
if op == "+":
    a = float(input("Number1: "))
    b = float(input("Number2: "))
    print(f"Result: {a + b}")

#subtraction method
elif op == "-":
    a = float(input("Number1: "))
    b = float(input("Number2: "))
    print(f"Result: {a - b}")

#multiplication method
elif op == "*":
    a = float(input("Number1: "))
    b = float(input("Number2: "))
    print(f"Result: {a * b}")

#division
elif op == "/":
    a = float(input("Number1: "))
    b = float(input("Number2: "))
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result: {a / b}")

#incorrect input
else:
    print("Invalid operator. Please choose +, -, *, /")