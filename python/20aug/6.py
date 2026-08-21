print("Program: Simple Calculator")
a = float(input("First number: "))
op = input("Operation (+, -, *, /, **, //): ")
b = float(input("Second number: "))

if op == "+":
    print("Output:", a + b)
elif op == "-":
    print("Output:", a - b)
elif op == "*":
    print("Output:", a * b)
elif op == "/":
    print("Output:", a / b)
elif op == "**":
    print("Output:", a ** b)
elif op == "//":
    print("Output:", a // b)
else:
    print("Output: Invalid operation")