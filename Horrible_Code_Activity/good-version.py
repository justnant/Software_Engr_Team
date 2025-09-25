#this is our good calc
#calc is slang for those who are new here
print("Calculator")
print("Choose +, -, *, /")
op = input("Op: ")

if op == "+":
    a = float(input("Number1: "))
    b = float(input("Number2: "))
    print(f"Result: {a + b}")

elif op == "-":
    a = float(input("Number1: "))
    b = float(input("Number2: "))
    print(f"Result: {a - b}")
    
elif op == "*":
    print()
elif op == "/":
    print()
else:
    print("Invalid operator. Please choose +, -, *, /")