#!/usr/bin/python3

print("=======Check a number's sign=======")
num=int(input("Enter a number to check if it is positive, negative or zero: "))

if num > 0:
    print(f"The number {num} you entered is positive.")

elif num < 0:
    print(f"The number {num} you entered is negative.")

else:
    print(f"The number {num} you entered is zero.")
   