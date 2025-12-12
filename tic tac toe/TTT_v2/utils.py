from datetime import datetime, time
from random import randint, choice
from time import sleep

class Player_Resources:
  winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
  turn_counter = 0
  board = dict()
  scorekeeper = {}

  def __init__(self, player=0, fname=None, token=None, claimed_space=None, go_first=0):
    self.player = player
    self.fname = fname
    self.token = token
    self.claimed_space = claimed_space
    self.go_first = go_first

  
  def greeting(self):
    """record player name and return a custom greeting based on time of day. When called, identifies the instance as a player"""
    self.player += 1
    now = datetime.now()
    if now.time() <= time(11,30):
      greet = "morning"
    elif now.time() <= time(12):
      greet = "afternoon"
    elif now.time() <= time(18):
      greet = "evening"
    else:
      greet = "night"
    
    name = input(f"""Good {greet}, challenger! What should I call you? 
: """)
    return greet, name
  
  def turn(self):
    if self == "cpu":
      move = Player_Resources.winning_combos[randint(0,8)][randint(0,2)]
      return move, self
    else:
      move = input("Your Move: ")
      self.claimed_space.append(move)
      return move, self

  

def thinking(x, personality=None):
  if not personality:
    personality = ["thinking", "hmmm", "let.. me.. see", "pondering my existence", "very interesting"]
    print(personality[randint(0,4)], end="", flush=True)
  else:
    print(personality, end="", flush=True)

  for i in range(x):
    sleep(.5)
    print(".", end="", flush=True)
  sleep(.5)
  print(".")
  sleep(.5)

def reset():
  for n in range(9):
    tile = f"tile_{n+1}"
    Player_Resources.board[tile] = ' '
  Player_Resources.scorekeeper["player"] = []
  Player_Resources.scorekeeper["cpu"] = []

def make_display_board():
  board = Player_Resources.board
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

def assign_tokens():
  player_token = input(f"""By default, game pieces are 'X' and 'O' but you can enter any character below and I will save that as your piece. 
If you have no preference, leave this prompt blank and I will randomly assign the pieces! 
: """)
  avail = ['X','O']
  if not player_token:
    player_token = avail.pop(randint(0,1))
    cpu_token = avail.pop(0)
  else:
    cpu_token = avail[randint(0,1)]
  return player_token, cpu_token

def coin_flip(name=None):
  """flip a coin to see who goes first"""
  if name:
    heads_or_tails = input(f"""Alright, {name}, time to get down to business. We will flip a coin to see who goes first. 
Please choose heads or tails (any character within 'heads' or 'tails' will also work). 
You may also say 'exit' to quit. 
: """).lower()
  else:
    heads_or_tails = input(":").lower()

  coin = ["heads", "tails"]
  result = coin.pop(randint(0,1))
    
  def flip_animation():
    print("\x1B[3mTing!\x1B[0m Flipping.", end="", flush=True)
    for i in range(3):         
      print(".", end="", flush=True)
      sleep(1)
    print(".")

  if heads_or_tails in result:
    flip_animation()
    print(f"{result}! You win!")
    return "player"
  elif heads_or_tails in coin:
    flip_animation()
    print(f"{result}! I win!")
    return "cpu"
  elif heads_or_tails in "exit":
    print("byee!")
    return "exit"
  elif heads_or_tails not in coin:
    if name:
      print(f"""Sorry, {name}, I don't recognize that input. Please say 'heads' or 'tails' or you can quit with 'exit'. 
: """)
    elif not name:
      print(f"""Sorry, I don't recognize that input. Please say 'heads' or 'tails' or you can quit with 'exit'.""")
    coin_flip()

def turn_service(move, instance):
  if move not in range
  instance.claimed_space += move