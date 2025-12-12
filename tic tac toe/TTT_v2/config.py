from utils import (
  Player_Resources
  ,coin_flip, thinking, reset, make_display_board, assign_tokens, turn_service
)

#entry point:
def main():
  #create player and computer instances within Resources class:
  player = Player_Resources()
  cpu = Player_Resources(0,"tic-tac-toby")

  #call greet method to set player fname:
  player.fname = Player_Resources.greeting(player)[1]
  print(f"Nice to meet you {player.fname}! My name is {cpu.fname} and this is tic-tac-toe!")

  #call token method to set player token and computer token:
  player.token, cpu.token = assign_tokens()
  thinking(2, "Setting your token.")
  print(f"Perfect! Your piece is {player.token} and mine is {cpu.token}")

  #call coin flip to determine turn order. if player inputs 'exit' then break out of main:
  coin_result = coin_flip(player.fname)
  if coin_result == "exit":
    return

  #reset and display board:
  thinking(1,"One moment, cleaning up the board.")
  reset()
  make_display_board()

  #begin turn order:
  if coin_result == "player":
    move, instance = player.move()
  elif coin_result == "cpu":
    move, instance = cpu.move()
  
  #delegate to turn_service:
    turn_service(move, instance)
  

main()