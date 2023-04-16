#Rock, paper, scissor game
def get_choices():
  player1_choice = input("Enter a choice player 1 (rock, paper, scissors): ")
  player2_choice = input("Enter a choice player 2 (rock, paper, scissors): ")
  choices = {"player1": player1_choice, "player2": player2_choice}
  return choices


def check_win(player1, player2):
  print(f"Player1 chose {player1}, Player2 chose {player2}")
  if player1 == player2:
    return "It's a tie!"
  elif player1 == "rock":
    if player2 == "scissors":
      return "Rock beats scissors! Player1 wins!"
    else:
      return "Paper beats rock! Player1 loses."
  elif player1 == "paper":
    if player2 == "rock":
      return "Paper beats rock! Player1 wins!"
    else:
      return "Scissors beats paper! Player1 loses."
  elif player1 == "scissors":
    if player2 == "paper":
      return "Scissors beats paper! Player1 wins!"
    else:
      return "Rock beats scissors! Player1 loses."


b = "yes"
while (b == "yes"):
  choices = get_choices()
  result = check_win(choices["player1"], choices["player2"])
  print(result)
  b = str(input("Do you want to start a new game? (yes/no): "))