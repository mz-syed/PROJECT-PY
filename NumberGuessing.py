#Number guessing game

import random

lowest_number = 1
highest_number = 100
guesses = 0
answer = random.randint(lowest_number, highest_number)

print("Welcome to the number guessing game!")
while True:
    guess = input("Guess a number between 1 and 100 :  ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("Guess should be between 1 and 100...")
        elif guess < answer :
            print("Too low, Try again...")
        elif guess > answer :
            print("Too high, Try again...")
        elif guess == answer :
            print()
            print(f"YOU GOT IT! It was {answer}.")
            break

    else:
        print("Invalid guess.")

print(f"You guessed the correct number in {guesses} tries.")