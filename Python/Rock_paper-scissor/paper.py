from random import randint
import utils

objs = ["Rock", "Paper", "Scissor"]

computer = objs[randint(0, 2)]

playing = True

while playing:
    player = input("Rock, Paper or Scissor ?    ")
    computer = objs[randint(0, 2)]
    
    print(utils.getWinner(player, computer))
    
    key = input(
        """
    1. To keep Playing Press Enter
    2. To Quit Press input Q
    """
    )
    if key == "q":
        playing = False

print("Thank You For Playing!")

