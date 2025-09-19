#!/usr/bin/python3

print("===== SIGN UP =====\n")
username = input('Enter username: ')
pwd = input('Enter password: ')
pwd2 = input('Enter password to confirm: ')

if pwd == pwd2:
    print('account has been successful created!')

print("===== Log In =====\n")

username2 = input('Enter username: ')
pwd3 = input("Enter password: ")

if pwd2 == pwd3 and username == username2:
    print("Login has been successful!")

else:
    print('Incorrent credintials, Please try again!')
