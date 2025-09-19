import random

print("Hi! welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the High Bound: "))

num = random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc +=1
    guess = int(input("Enter your guess: "))
    if guess == num:
        print("Yeh! You won.")
        break

    elif gc >= ch and guess != num:
        print("Sorry, You lost!")

    elif guess > num:
        print("High")

    elif guess < num:
        print("Low")
