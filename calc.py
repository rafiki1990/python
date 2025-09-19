#!/usr/bin/python3

num1 = float(input("Enter a first number: "))
operator = input("Enter an operator: ")
num2 = float(input("Enter a second number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("Invalid oparator!")