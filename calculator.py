num1 = float(input("Enter first number:   "))
op = input("Enter + , - , / , * , ^   ")
num2 = float(input("Enter second number:   "))

if op== "-" :
    print(num1 - num2)
elif op== "+":
    print(num1 + num2)
elif op=="/":
    print(num1 / num2)
elif op== "*":
    print(num1*num2)
elif op== "^":
    x = pow(num1,num2)
    print(x)
else:
    print("invalid operator")

input("press Enter to Exit")