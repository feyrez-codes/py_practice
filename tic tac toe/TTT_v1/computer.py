import random 
def computer_move():
  global computer_strategy #escape strategy var
  global turn_counter
  print(turn_counter)
  print("starting computer move..")
  #if first turn, pick a strategy to pursue:
  if turn_counter == 2:
    computer_strategy += random.choices(winning_combos, weights=winning_combos_probability)
    scorekeeper["cpu"].append(computer_strategy[0][random.randint(0,2)])
    turn_counter += 1
    print('made it to cpu move')
    turn_service()
      
  #if not first turn, play a reactive strategy:
  if turn_counter > 2:

    #check if player has blocked cpu chosen strategy:
    continue_with_strategy = True
    for x in scorekeeper["player"]:
      if x in computer_strategy:
        continue_with_strategy = False
        break    
    if not computer_strategy:
      continue_with_strategy = False

    #if player has not blocked chosen strategy, pick a move from chosen to play, removing any that have been played by cpu already:
    if continue_with_strategy == True:
      for x in scorekeeper["cpu"]:
        if x in computer_strategy:
          computer_strategy.remove(x)
      return(computer_strategy[random.randint(0,len(computer_strategy)-1)])

    #if player has blocked cpu chosen strategy, choose new one based on player move:
    if continue_with_strategy == False:
      player_win_conditions = list()

      #catalogue possible win combos for player (catalogue = "player_win_conditions"(unparsed)):
      for combo in winning_combos:
        for move in scorekeeper["player"]:
          if move in combo:
            player_win_conditions.append(combo)

      #remove duplicates from player catalogue ("player_viable_moves" (parsed)):
      for x in range(1,5): #for loop here: since the same combo can be added more than once, pass over List of Lists multiple times
        for combo in player_win_conditions:
          for num in scorekeeper["cpu"]:
            if num in combo and combo in player_win_conditions:
              player_win_conditions.remove(combo)
      player_viable_moves = list(map(list, dict.fromkeys(map(tuple, player_win_conditions))))  

      #With player viable moves catalogued, catalogue possible winning strategies for cpu based on moves played:
      temp_move_choice = list()
      for combo in winning_combos:
        #when CPU has made 1 move:
        if scorekeeper["cpu"] in combo and len(scorekeeper["cpu"]) == 1:
          temp_move_choice.append(combo)
        #when CPU has made 2 moves:
        elif set(scorekeeper["cpu"]).issubset(set(combo)) and len(scorekeeper["cpu"]) == 2:
          temp_move_choice.append(combo)
        #when CPU has made 3 or more moves:
        elif len(scorekeeper["cpu"]) > 2:
          for move in scorekeeper["cpu"]:
            for move in combo:
              temp_move_choice.append(combo)
      
      #return overlapping strategies:
      cpu_viable_moves = list()
      for player_move in player_viable_moves:
        for cpu_move in temp_move_choice:
          if cpu_move == player_move:
            cpu_viable_moves.append(cpu_move)
      if not cpu_viable_moves:
        cpu_viable_moves = player_viable_moves

      #pick SMARTLY from final pool of strategies:
      for combo in cpu_viable_moves:
        for tile in scorekeeper["player"]:
          if tile in combo:
            combo.remove(tile)
        for tile in scorekeeper["cpu"]:
          if tile in combo:
            combo.remove(tile)
      scorekeeper["cpu"].append(combo[0])
      turn_counter += 1
      turn_service()