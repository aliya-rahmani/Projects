#snakes and ladders

import random
def makeBoard(n):
    i = 1
    board = [] #empty
    while i <= 100:
        element = [i, [' ']*n, ' ']
        board.append(element) #expand
        i+=1
    return board

def displayBoard(board):
    i = 1
    x = 99
    flag = 0
    while i <=10:
        print()
        j = 1
        while j <=10:
            print(board[x], end=' ')
            #var = valOnTrue if condn else valOnFalse
            x = x-1 if flag == 0 else x+1
            j+=1
        x = x-9 if flag == 0 else x - 11
        flag = (flag +1 )%2
        i+=1

def autodice():
    totDice = 0
    while totDice< 18:
        #dice
        x = random.randint(1,6)#a random number in range 1-6
        totDice+= x
        print('Current dice value:',x)

        if x != 6:
            break
    return  totDice%18

def dice():
    totDice = 0
    while totDice< 18:
        if len(input('press enter to dice')) == 0:
            #dice
            x = random.randint(1,6)#a random number in range 1-6
            totDice+= x
            print('Current dice value:',x)

            if x != 6:
                break
    return  totDice%18

def setupPlayers():
    symbol_score_bank= [['♥',0],['♦',0],['♣',0],['♠',0]] #alt+3, alt+4, alt+5, alt+6
    system = ['☺',0] #alt+1
    players = []
    while True:
        x = int(input('Enter the number of players(1-4)'))
        if x == 1:
            if input('Do you want to play with System (y/n) : ').lower() == 'y':
                players.append(symbol_score_bank[0])
                players.append(system)
                break
        elif x >=2 and x <=4:
            i =0
            while i < x:
                players.append(symbol_score_bank[i])
                i+=1
            break
        else:
            print('Wrong Choice')

    return players #list

def snakes_and_ladders():
    players = setupPlayers()
    board = makeBoard(len(players))

    current = 0
    while len(players) > 1:
        displayBoard(board)
        print(players[current][0] + ' to play ')
        if players[current][0] == '☺':
            print('System Plays: ')
            moveVal = autodice()
        else:
            moveVal =  dice()
        print('To move by: ', moveVal)

        if players[current][1] + moveVal <=100:
            #remove player symbol from board[pos1]
            board[players[current][1]-1][1][current] = ' '
            #update score
            players[current][1]+=moveVal
            #add player symbol to board[pos2]
            board[players[current][1]-1][1][current] = players[current][0]

            if players[current][1] == 100:
                print(players[current][0], 'WINS')
                players.pop(current) #remove
        else:
            print(players[current][0] , ' needs ', (100- players[current][1]))

        current = (current+1) % len(players)

    print(players[0], 'LOSES!!!')

def main():
    snakes_and_ladders()

main()