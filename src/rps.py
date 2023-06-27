def rock_paper_scissors(player_choice, computer_choice):
    if player_choice == "rock":
        if computer_choice == "rock":
            return "Tie!"
        elif computer_choice == "paper":
            return "You lose!"
        elif computer_choice == "scissors":
            return "You win!"
        else:
            return "Invalid choice!"
    elif player_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        elif computer_choice == "paper":
            return "Tie!"
        elif computer_choice == "scissors":
            return "You lose!"
        else:
            return "Invalid choice!"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "You lose!"
        elif computer_choice == "paper":
            return "You win!"
        elif computer_choice == "scissors":
            return "Tie!"
        else:
            return "Invalid choice!"
    else:
        return "Invalid choice!"
