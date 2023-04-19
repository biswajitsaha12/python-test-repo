#Rock, paper, scissor game
from getpass import getpass
import re

def get_choices():
  player1_choice = getpass("Enter a choice player 1 (rock, paper, scissors): ")
  player1_choice = player1_choice.lower()
  player2_choice = getpass("Enter a choice player 2 (rock, paper, scissors): ")
  player2_choice = player2_choice.lower()
  choices = {"player1": player1_choice, "player2": player2_choice}
  return choices

def check_win(player1, player2):
  #print(f"Player1 chose {player1}, Player2 chose {player2}")
  if not re.search(r"^(rock$|paper|scissors)$",player1) and not re.search(r"^(rock|paper|scissors)$",player2):
    return "Invalid choice by both Players"
  elif not re.search(r"^(rock$|paper|scissors)$",player1):
    return "Invalid choice selected by player1, Player2 Wins!"
  elif not re.search(r"^(rock|paper|scissors)$",player2):
    return "Invalid choice selected by player2, Player1 Wins!"
  elif player1 == player2:
    return "It's a tie!"
  elif player1 == "rock":
    if player2 == "scissors":
      return "Rock beats scissors! Player1 wins!"
    else:
      return "Paper beats rock! Player2 wins!"
  elif player1 == "paper":
    if player2 == "rock":
      return "Paper beats rock! Player1 wins!"
    else:
      return "Scissors beats paper! Player2 wins!"
  elif player1 == "scissors":
    if player2 == "paper":
      return "Scissors beats paper! Player1 wins!"
    else:
      return "Rock beats scissors! Player2 wins!"
  else:
    return "Invalid choice selected, please restart"


b = "y"
while (b == "y"):
  choices = get_choices()
  result = check_win(choices["player1"], choices["player2"])
  print(result)
  b = str(input("Do you want to start a new game? (y/n): "))