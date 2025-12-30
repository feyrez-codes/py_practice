from utils import (
                    greeting, thinking, coin_flip, cpu_matrix,
                    Make_board, Scorekeeper
                  )
from random import randint

def main():
  name, player_token, cpu_token = greeting()

  thinking(2, "jotting that down")

  print(f"""Very well, {name} it is decided. You shall wield {player_token} and I will be {cpu_token}'s.
Familiarize yourself with our game board while I prepare the coin flip:""")
  
  board = Make_board.setup()[0]
  print(board)

  thinking(5, "let me find a coin")

  flip_message, player_first = coin_flip(name)

  print(flip_message)

  if player_first:
    first_move = input("""Your Move: """)
    while first_move not in range(1,10):
      first_move = input("""Please select a number between 1-9: """)
    player = Scorekeeper(first_move)
  else:
    first_move = cpu_matrix([], [])
    cpu = Scorekeeper(first_move)


if __name__ in "__main__":
  main()