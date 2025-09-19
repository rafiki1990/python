#!/usr/bin/python3

print("=========Unit Converter==========")
print("Options:temp,length")

option = input("Enter your option: ")

if option == "temp":
    celsius = float(input("Enter the Celsius to converter in Fahrenheit: "))
    fahrenheit = (celsius * (9/5) + 32)
    print(f"Fahrenheit is: {fahrenheit}°F")

elif option == "length":
    meter = float(input("Enter the value of length in meters to converter in kilometer: "))
    kilometer = meter / 1000
    print(f"kilometer is {kilometer}")

else:
    print("Option not found, try again!")
