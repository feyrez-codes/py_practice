from random import randint, choice
from time import sleep

class Scorekeeper:
  """
  :Purpose: This class manages the storage of game variables and turn governance.
  :Params: move_1: instance creation requires the first move of the new instance (each instance represents a player: one human, one cpu for this module)
  """
  winning_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
  players = []
  chosen_tiles = []

  def __init__(self, move_1, player_token):
    self.moveset = [move_1]
    self.name = self
    self.token = player_token
    Scorekeeper.players.append(str(self))
    Board.board_array[f"slot_{move_1}"] = self.token

    if len(self.moveset) > 0: 
      for move in self.moveset:
        if move not in Scorekeeper.chosen_tiles: Scorekeeper.chosen_tiles.extend(move) 

      
  @staticmethod
  def turn_service(cpu, player):
    """
    :Purpose: evaluate the given instances against array_evaluator. For both players and the cpu bot, this method determines when the game has been won. 
    \nFor cpu, this method calls on function cpu_matrix to return a viable next move if the game is to continue.
    
    :Params: instances: a list of the two class instances used in this tic-tac-toe game
    """
    cpu_combos, cpu_nearwin, player_combos, player_nearwin = array_evaluator(Scorekeeper.winning_combos
                    , cpu.moveset
                    , player.moveset)
    


    
class Board:
  board_array = {}

  @staticmethod
  def setup():
    """
    :Purpose: Create first time array to track token positions. Intended only to be called once or to reset game board.
    """
    for x in range(1,10):
      slot = f"slot_{x}"
      Board.board_array[slot] = str(x)

  @staticmethod
  def display():
    """
    :Purpose: Map board_array dictionary into a gameboard visualization.
    """
    board = """"""""
    for x in range(1,10):
      if x in (1,2,4,5):
        board += ('_' + "\x1B[4m" + Board.board_array[f"slot_{x}"] + "\x1B[0m" + '_' + '|')
      elif x in [3,6]:
         board += ('_' + "\x1B[4m" + Board.board_array[f"slot_{x}"] + "\x1B[0m" + '_' +'\n')
      elif x in [7,8]:
         board += ' ' + Board.board_array[f"slot_{x}"] +  ' ' + '|'
    else:
       board += ' ' + Board.board_array[f"slot_{x}"]
       board +="""
"""
    print(board)

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
  
  player_selection = input(f"""Alright, {name}, call it. Heads or tails? 
(You may also give me unique characters like "H" for heads or "t" for tails.)
:""")
  
  while player_selection.lower() not in "heads" and player_selection.lower() not in "tails":
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
  :Purpose: Evaluate given list(s) as part of a superset. Initially created to generate intelligent predictions for a tic-tac-toe bot.

  :Param: superset: list to be compared for subset combination matches
  :Param: *subset: list(s) to be compared as subsets to superset arg. 
    \nex: [1,2,3] returns [[1,2], [1,3], [2,3]]
  :Param: readable: See below for output if False. if True, the function will output a dictionary with two key values: "array_{x}_combos", "array_{x}_matches" where x = arg index +1.

  :Output: every subset returns an list of two lists, matching the argument index
    \nList 1: Every possible combinations of the subset, up to 3 digit combos
    \nList 2: All partial or full match between list 1 and superset. Note:
        \nIf no matches are found, the second list will be empty
        \nex: a superset of [1,2,3] and a subset of [1,2,3] would return [1,2], [1,3] and [2,3] as partial matches and [1,2,3] as a whole match. 
  """
  def mini_evaluator(target, test):
    """
    Purpose: convert both arguments to sets then check if test arg is subset of target arg

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

def cpu_matrix(opponent_win_paths, my_win_paths, unchoosable):
  """
  :Purpose: Ingest two lists, each containing possible winning combinations for players in a tic-tac-toe game, and return my best move choice given context

  :Param: opponent_win_paths: a list of 3 digit lists, each representing possible combinations my opponent could follow to defeat me
  :Param: my_win_paths: a list of lists, each containing possible combinations that I can take to win the game
  :Param: unchoosable: any moves that cannot be picked (in tic-tac-toe, any tile that has already been claimed)
  \nExample: param 1 = [3, 6, 9] (my opponent has played 6, 9). param 2 = [1, 2, 3], [1, 5, 9], [1,4,7] (I have played 1). Output would be 3 as it both furthers my game plan and thwarts my opponent.
  \nExample: param 1 = [3, 6, 9] (my oppponent has played 6, 9). param 2 = [7, 8, 9], [2, 5, 8] (I have played 8). Output would be 3 as preference is given to thwarting my opponent

  :Output: The best move, of course
  """

  next_move = []

  #choose overlaps
  for combo in opponent_win_paths:
    for ideal in my_win_paths:
      if combo == ideal:
        next_move.extend(combo)

  #if no overlap
  if not next_move:
    for combo in opponent_win_paths:
      next_move.extend(combo)

  return choice([num for num in next_move if num not in unchoosable])