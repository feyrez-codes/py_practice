from random import randint
from time import sleep

class Scorekeeper:
  """
  :Purpose: This class manages the storage of game variables and turn governance.
  :Params: move_1: instance creation requires the first move of the new instance (each instance represents a player: one human, one cpu for this module)
  """
  winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
  players = []

  def __init__(self, move_1):
    self.moveset = [move_1]
    Scorekeeper.players.append(str(self))
      
  def move(self):
    if self == "player":
      player_move = input("Your move: ")
      self.moveset.append(player_move)

    elif self == "cpu":

      self.moveset.append()

    self.turn_service()
  
  def turn_service(self):
    possible_wins = [array for array in self.moveset if len(array) == 3]

    for combo in possible_wins:
      if combo.sort() in Scorekeeper.winning_combos:
        return f"{self} wins!"
    else:
      return Scorekeeper.players[Scorekeeper.players.index(self)-1]


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


def array_evaluator(superset: list, *subset: list, readable: bool=False) -> list:
  """
  :Purpose: Evaluate (a) given list(s) as part of a superset. Initially created to generate intelligent predictions for a tic-tac-toe bot.

  :Param: superset: list to be compared for subset combination matches
  :Param: *subset: list(s) to be compared as subsets to superset arg. 
    \nex: [1,2,3] returns [[1,2], [1,3], [2,3]]
  :Param: readable: If false, output remains as detailed below. if True, the function will return a dictionary with two key values: "array_{x}_combos", "array_{x}_matches" where x = arg index +1.

  :Output: every subset returns an list of two lists, matching the argument index
    \nList 1: Every possible combinations of the subset, up to 3 digit combos
    \nList 2: All partial or full match between list 1 and superset. Note:
        \nIf no matches are found, the second list will be empty
        \nex: a superset of [1,2,3] and a subset of [1,2,3] would return [1,2] as a partial combination. 
  """
  def mini_evaluator(target, test):
    """
    Purpose: convert both arguments to set then check if test is subset of target

    :Params: test: value to be searched for in target
    :Params: target: superset to be scrutinized for presence of test

    :Output: returns test if test is subset of target
    """
    x = set(target)
    y = set(test)
    if (x == y or y.issubset(x)): return list(y)

  expanded_array = []
  if readable: final_array = {}
  else: final_array = []

  for array in subset:
    if readable:
        combo_dkey = f"array_{subset.index(array)+1}_combos"
        match_dkey = f"array_{subset.index(array)+1}_matches"

    #create all combinations
    for seed in array:
      for stem in array:
        if seed != stem:

          #create groups of two:
          x = sorted([seed, stem])
          if x not in expanded_array:
            expanded_array.append(x)

          #create groups of three:
          for leaf in array:
            y = sorted([seed, stem, leaf])

            if (seed != leaf != stem and y not in expanded_array):
              expanded_array.append(y)
    
    #compare combinations to superset:    
    matches = []
    for array in expanded_array:
      if not isinstance(superset[0], list):
        matches.append(mini_evaluator(superset , array))
      else:
        for combo in superset:
          matches.append(mini_evaluator(combo, array))

    if readable:
      final_array[combo_dkey] = matches
      final_array[match_dkey] = expanded_array
    else:
      final_array.append(expanded_array)
      final_array.append(list(filter(None, matches)))

  return final_array