
def getWinner(player, computer):
    if player == "Rock":
        if computer == "Scissor":
            return f"You Win!!, {player} Beats {computer}"
        elif computer == "Paper":
            return f"You Lose, {computer} Beats {player}"
        else:
            return "Draw"
    elif player == "Paper":
        if computer == "Rock":
            return f"You Win!!, {player} Beats {computer}"
        elif computer == "Scissor":
            return f"You Lose, {computer} Beats {player}"
        else:
            return "Draw"
    elif player == "Scissor":
        if computer == "Paper":
            return f"You Win!!, {player} Beats {computer}"
        elif computer == "Rock":
            return f"You Lose, {computer} Beats {player}" 
        else:
            return "Draw"
    else:
        return "Check your spelling"
