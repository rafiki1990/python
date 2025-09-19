num = int(input("Enter a number to check if is Even or Odd: "))

if num % 2 == 0:
    print(f'The number {num} is Even')
elif num % 2 == 1:
    print(f'The number {num} is Odd')
else:
    print('Invalid')