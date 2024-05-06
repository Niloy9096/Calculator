n = float(input("Enter number1: "))
o = input("Enter Operator: ")
m = float(input("Enter number2: "))

if o == "+":
    print(n + m)
elif o == "-":
    print(n - m)
elif o == "*":
    print(n * m)
elif o == "/":
    if m != 0:
        print(n / m)
    else:
        print("Error!")
else:
    print("Invalid operator")
