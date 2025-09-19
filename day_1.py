#!/usr/bin/python3

#Variable & Data types
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you will be {age + 10} in 10 years.")

cel = int(input("Enter the value of celsius: "))
fah = (cel * (9/5) + 32)
print(f"{cel}°C = {fah}°F")