# This is our bad calculator

print("Calculator")
print("Choose +, -, *, /")
op = input("Op: ")

if op == "+":
    a= float(input("Number1: "))
    b= float(input("Number2: "))
    print("Result:" + str(a + b))
if op== "-":
    x = float(input("Enter num: "))
    y = float(input("Enter num again: "))
    print("Answer is " + str(x - y))
if op == "*":
    n1 = float(input("Enter n1: "))
    n2 = float(input("Enter n2: "))
    print("Product: " + str(n1 * n2))
if op == "/":
    i = float(input("first: "))
    j = float(input("second: "))
    if j== 0:
        print("Error, divide by zero? Really?")
    else:
        print("Quotient is " + str(i / j))
        