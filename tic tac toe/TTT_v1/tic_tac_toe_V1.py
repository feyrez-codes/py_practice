import random
import time 






#Game pieces:
scorekeeper = {}
board = dict()
player_token = str()
computer_token = str()
winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
winning_combos_probability = [.08 , .2 , .08 , .08 , .2 , .08 , .08 , .2 ]
computer_strategy = list()





#create board, reset scorekeeper
def reset():
  for n in range(9):
    tile = f"tile_{n+1}"
    board[tile] = ' '
  scorekeeper["player"] = []
  scorekeeper["cpu"] = []
reset()

print(scorekeeper)




def entry():
  #set tokens, collect player name
  global computer_token 
  global player_token
  global turn_counter
  tokens = ["X", "O"]
  computer_token += tokens.pop(random.randint(0,1))
  player_token += tokens[0]
  print(f"Hello, {name}! You shall be {player_token}s. I will take {computer_token}s. Here is our game board:")

  #show empty board and give time for view
  utils.make_display_board()
  time.sleep(2)

  #set up coin flip
  print("Please wait while I prepare our coin flip!")
  time.sleep(3)

  #perform coin flip

  #inner func for "bad input" handling
  def inner_coin_flip():
    heads_or_tails = input(f"""Alright, {name}, would you prefer Heads or Tails? """).lower()
    global coin 
    global face
    coin = random.randint(0,1)
    if heads_or_tails in "heads":
      face = 0
    elif heads_or_tails in "tails":
      face = 1
    elif heads_or_tails in "exit":
      print("Goodbye!")
    else:
      print("Sorry! That input is not valid. Please say heads or tails, or you can exit by saying exit!")
      inner_coin_flip()
  inner_coin_flip()

  #flipping "animation"
  print("\033[3mting!\033[0m flipping.")
  time.sleep(.5)
  for n in range(2,4):
    print(f"flipping{"."*n}")
    time.sleep(.5)
  
  #confirm which face lands:
  if coin == 0:
    print ("Heads!")
    time.sleep(1)
  elif coin == 1:
    print("Tails!")
    time.sleep(1)

  #reveal coinflip winner:
  if face == coin:
    print(f"Very Good! You may go first, {name} ")
    utils.make_display_board()
    turn_counter = 1
    time.sleep(2)
    utils.player_move(player_token)
  if face != coin: 
    print("Uh Oh! Looks like I go first.")
    turn_counter = 2
    time.sleep(3)
    computer_move()

  #start point: 
name = input("Hello! What is your name, challenger? ")  
