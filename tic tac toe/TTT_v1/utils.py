import random
import time
from TTT_v1.computer import winning_combos, computer_move, turn_counter

#Game pieces code:
scorekeeper = {}



def make_display_board():
  print("""
    Key:
   1 2 3
   4 5 6
   7 8 9""")
  tic_tac_toe_board = """
"""
  for n in range(len(board)):
    if n+1 in [1,2,4,5]:
      tic_tac_toe_board += ('_' + "\x1B[4m" + board[f"tile_{n+1}"] + "\x1B[0m" + '_' + '|')
    elif n+1 in [3,6]:
      tic_tac_toe_board += ('_' + "\x1B[4m" + board[f"tile_{n+1}"] + "\x1B[0m" + '_' +'\n')
    elif n+1 in [7,8]:
      tic_tac_toe_board += ' ' + board[f"tile_{n+1}"] +  ' ' + '|'
    else:
      tic_tac_toe_board += ' ' + board[f"tile_{n+1}"]
  tic_tac_toe_board +="""
"""
  print(tic_tac_toe_board)

def player_move(p_token):
  global turn_counter
  player_tile = int(input("Your move: "))
  if player_tile not in range(1,10):
    print("Sorry, that move is not valid! choose another.")
    player_move()
  elif board[f"tile_{player_tile}"] == ' ':
    board[f"tile_{player_tile}"] = p_token # player piece
  else:
    if player_tile in scorekeeper["player"]:
      print("You've already claimed that tile, choose another one! ")
      player_move()
    elif player_tile in scorekeeper["cpu"]:
      print("Hey! I've already played on that tile! Pick another one!")
      player_move()
  make_display_board()

  scorekeeper["player"].append(int(player_tile))
  
  turn_counter += 1
  turn_service(p_token)

#check for winner and push action to next player:
def turn_service(token):
  global turn_counter
  for combo in winning_combos:
    if set(combo) == set(scorekeeper["player"]):
      print("you win!")
      break
    elif set(combo) == set(scorekeeper["cpu"]):
      print("you lose!")
      break
    else:
      continue
  if not turn_counter%2:
    computer_move(token)
  elif turn_counter%2:
    player_move(token)