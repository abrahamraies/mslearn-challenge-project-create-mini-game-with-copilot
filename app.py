# create a rock, paper, scissors minigame, following the next rules:
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def rock_paper_scissors():
    player_score = 0
    computer_score = 0
    while True:
        player = input("Choose rock, paper, or scissors: ")
        computer = random.choice(["rock", "paper", "scissors"])
        if player.lower() not in ["rock", "paper", "scissors"]:
            print("Invalid option, please choose rock, paper, or scissors.")
            continue
        print(f"Computer chose {computer}.")
        if player.lower() == computer:
            print("It's a tie!")
        elif player.lower() == "rock" and computer == "scissors":
            print("You won!")
            player_score += 1
        elif player.lower() == "scissors" and computer == "paper":
            print("You won!")
            player_score += 1
        elif player.lower() == "paper" and computer == "rock":
            print("You won!")
            player_score += 1
        else:
            print("You lost!")
            computer_score += 1
        print(f"Player score: {player_score}, Computer score: {computer_score}")
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            break
    print(f"Final score: Player {player_score} - {computer_score} Computer")

rock_paper_scissors()