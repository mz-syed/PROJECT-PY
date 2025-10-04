# Game of rock, paper, scissors

import random

game = ("rock", "paper", "scissors")
computer = random.choice(game)

while True:
    player = input("Choose rock, paper or scissors : ")
    print(f"You - {player:10}")
    print(f"Computer - {computer:10}")

     elif player == "rock" and computer == "scissors":
        print()
        print("YOU WIN!")
        print(f"{player} beats {computer}.")

    elif player == "paper" and computer == "rock":




