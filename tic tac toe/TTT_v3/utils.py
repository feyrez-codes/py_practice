from random import randint
from time import sleep
import itertools

class Scorekeeper:
  """
  This class manages the storage of game variables and turn governance.

  """
  winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
  players = []

  def __init__(self, move_1):
    self.moveset = [move_1]
    Scorekeeper.players.append(self)
      
  def move(self):
    if self == "player":
      player_move = input("Your move: ")
      self.moveset.append(player_move)

    elif self == "cpu":
      self.moveset.append()
  
  def turn_service(self):
    if Scorekeeper.snowflake_compare(self.moveset):
      return f"{self} wins!"
    else:
      return Scorekeeper.players[Scorekeeper.players.index(self)-1]

  @staticmethod
  def snowflake_compare(array: list) -> list:
    """
    Breaks down an array into every combination of the contents, then compares the remapped data to the winning combos.

    returns: 1 for win, 0 for no win
    """
    transformed = (list(combo) for combo in list(itertools.combinations(array, 3)))
    
    for arr in transformed:
        for combo in Scorekeeper.winning_combos:
          if arr == combo:
              return 1
    return 0


class Make_board:
  board_array = {}
  board = """"""""

  @staticmethod
  def setup():
    for x in range(1,10):
      slot = f"slot_{x}"
      Make_board.board_array[slot] = str(x)
    return Make_board.show()
      
  @staticmethod
  def show():
    for x in range(1,10):
      if x in (1,2,4,5):
        Make_board.board += ('_' + "\x1B[4m" + Make_board.board_array[f"slot_{x}"] + "\x1B[0m" + '_' + '|')
      elif x in [3,6]:
         Make_board.board += ('_' + "\x1B[4m" + Make_board.board_array[f"slot_{x}"] + "\x1B[0m" + '_' +'\n')
      elif x in [7,8]:
         Make_board.board += ' ' + Make_board.board_array[f"slot_{x}"] +  ' ' + '|'
    else:
       Make_board.board += ' ' + Make_board.board_array[f"slot_{x}"]
       Make_board.board +="""
"""
    return Make_board.board, Make_board.board_array

def greeting():
  name = input("""Greetings, Challenger! What shall I call you?
:""")

  player_token = input(f"""Nice to meet you, {name}! My name is tic-tac-toby and this is tic-tac-toe!
The object of this game is to claim three tiles in a row on a 3x3 gameboard. 
Traditionally, our game tokens are 'X' and 'O'. If you'd like a custom game token, please enter it below or leave it blank and I will select your token for you.
:""")

  default_tokens = ["X", "O"]
  cpu_token = default_tokens.pop(randint(0,1))
  if not player_token:
    player_token = default_tokens[0]

  return name, player_token, cpu_token


def thinking(x, personality=None):
  """
  :param: x (int): interval of sleep in .5 seconds.
  :param: personality (str): message to be displayed
  """
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


def coin_flip(name="player"):
  coin = ["heads", "tails"].pop(randint(0,1))
  
  player_selection = input(f"""Alright, f{name}, call it. Heads or tails? 
(You may also give me unique characters like "H" for heads or "t" for tails.)
:""")
  
  while player_selection.lower() not in "heads" and player_selection not in "tails":
    print("Sorry, that selection is not valid")
    player_selection = input("""Please pick heads or tails, or you can type 'exit' to quit.
:""")

  while player_selection.lower() in "heads" and player_selection.lower() in "tails":
    print("Sorry, that selection is ambiguous!")
    player_selection = input("""Please type 'heads', 'tails' or you can type 'exit' to leave.
:""")
  
  if player_selection in 'tails':
    player_selection = 'tails'
    if coin == 'tails':
      return "tails, you go first!", 1
  elif player_selection in 'heads':
    player_selection = 'heads'
    if coin == 'heads':
      return "heads, you go first!", 1

  return f"{coin}! Better luck next time; looks like I shall be going first!", 0


def array_evaluator(*subset: list) -> dict:
  """
  :Purpose: break down lists into each possible combination of each submitted list.

  :Param: *subset: list(s) to be compared as subsets to superset arg. 
    ex: [1,2,3] returns [[1,2], [1,3], [2,3]]

  :Output: returns a dict of each possible combination, broken down by positional array.
  """
  expanded_array = {}
  for array in subset:
    arr_name = f"array_{subset.index(array)+1}"
    expanded_array[arr_name] = []

    for seed in array:
      x = [seed]

      for stem in array:
        if stem == seed:
          pass
        else:
          x.append(stem)
          x.sort()
          if x not in expanded_array[arr_name]: 
            expanded_array[arr_name].append(x)
            x = [seed]

  return expanded_array

def cpu_matrix(my_moves, opp_moves):
  viable_moves = [num for num in range(1,10) if num not in my_moves + opp_moves]

  array_evaluator(Scorekeeper.winning_combos, my_moves, opp_moves)


  #should I attack or defend?
  DANGER = snowflake()