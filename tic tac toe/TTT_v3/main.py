from utils import (
                    greeting, thinking, coin_flip, cpu_matrix,
                    Board, Scorekeeper
                  )
from random import randint

def main():
  name, player_token, cpu_token = greeting()

  thinking(2, "jotting that down")

  print(f"""Very well, {name} it is decided. You shall wield {player_token} and I will be {cpu_token}'s.
Familiarize yourself with our game board while I prepare the coin flip:""")
  
  Board.setup()
  Board.display()

  thinking(5, "let me find a coin")

  flip_message, player_first = coin_flip(name)

  thinking(2,"flipping...")

  print(flip_message)

  #first move
  Board.display()
  if player_first:
    first_move = int(input("""Your Move: """))
    while first_move not in range(1,10):
      first_move = input("""Please select a number between 1-9: """)
    player = Scorekeeper(first_move, player_token)
  else:
    first_move = randint(1,10)
    cpu = Scorekeeper(first_move, cpu_token)

  #second move
  Board.display()
  if player_first:
    win_paths = [combo for combo in Scorekeeper.winning_combos if set([*player.moveset]).issubset(set(combo))]

    second_move =  cpu_matrix(win_paths, [], Scorekeeper.chosen_tiles)
    
    cpu = Scorekeeper(second_move, cpu_token)



  #begin move sequence:
  while not Scorekeeper.turn_service(cpu, player):
    pass




if __name__ in "__main__":
  main()