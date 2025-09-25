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