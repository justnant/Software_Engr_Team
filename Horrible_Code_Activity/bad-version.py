#  Justin & Gabriel Calc
# This is our bad calculator

print("Calculator")
print("Choose +, -, *, /")
op = input("Op: ")

if op == "+":
    a= float(input("Enter num1: "))
    b= float(input("Enter num2: "))
    print("Result:" + str(a + b))
if op== "-":
    x = float(input("Enter num1: "))
    y = float(input("Enter num2: "))
    print("Answer is " + str(x - y))
if op == "*":
    n1 = float(input("Enter num1: "))
    n2 = float(input("Enter num2: "))
    print("Product: " + str(n1 * n2))
if op == "/":
    i = float(input("Enter num1: "))
    j = float(input("Enter num2: "))
    if j== 0:
        print("Error, divide by zero? Really?")
    else:
        print("Quotient is " + str(i / j))
        