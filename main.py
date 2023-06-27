# Write a rock, paper, scissors game
# 1. Player vs Computer
# 2. First to 3 wins

import random
from src.rps import rock_paper_scissors

def main():
    player_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("First to 3 wins!")

    while player_score < 3 and computer_score < 3:
        player_choice = input("Choose rock, paper, or scissors: ")
        computer_choice = random.randint(1, 3)
        if computer_choice == 1:
            computer_choice = "rock"
        elif computer_choice == 2:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"

        print("Computer chose: " + computer_choice)

        result = rock_paper_scissors(player_choice, computer_choice)
        print(result)
        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            computer_score += 1

        print("Player: " + str(player_score))
        print("Computer: " + str(computer_score))

if (__name__ == "__main__"):
    main()