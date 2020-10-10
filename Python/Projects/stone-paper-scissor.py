import random

while True:
    player = input("stone, paper, scissor? : ")
    computer = random.choice(['stone' , 'paper' , 'scissor'])

    if player == computer:
        print("Tie!")
    elif player == "stone":
        if computer == "paper":
            print(" You lose! :( " , computer , "covers " , player)
        else:
            print(" You win! :) " , player , "smashes ", computer)
    elif player == "paper":
        if computer == "scissor":
            print(" You lose! :( " , computer , "cuts " , player)
        else:
            print("You win! :) " , player , "covers " , computer)
    elif player == "scissor":
        if computer == "stone":
            print(" You lose! :( ", computer , "smashes ", player)
        else:
            print("You win! :) ", player , "cuts ", computer)
    else:
        print("Please, check your spelling! :]")
