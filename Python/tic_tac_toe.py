theBoard = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
def check_win():
    if theBoard[1] == theBoard[2] == theBoard[3] != ' ':
        printBoard(theBoard)
        print(turn, 'wins')
        exit()
    elif theBoard[1] == theBoard[4] == theBoard[7] != ' ':
        printBoard(theBoard)
        print(turn, 'wins')
        exit()
    elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':
        printBoard(theBoard)
        print(turn, 'wins')
        exit()
    elif theBoard[2] == theBoard[5] == theBoard[8] != ' ':
        printBoard(theBoard)
        print(turn, 'wins')
        exit()
    elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':
        printBoard(theBoard)
        print(turn, 'wins')
        exit()
    elif theBoard[3] == theBoard[5] == theBoard[7] != ' ':
        printBoard(theBoard)
        print(turn, 'wins')
        exit()
    elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':
        printBoard(theBoard)
        print(turn, 'wins')
        exit()
    elif theBoard[7] == theBoard[8] == theBoard[9] != ' ':
        printBoard(theBoard)
        print(turn, 'wins')
        exit()
    elif i == 8:
        printBoard(theBoard)
        print('Ties')
        exit()
    else:
        pass

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


turn = 'X'
print('1' + '|' + '2' + '|' + '3')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('7' + '|' + '8' + '|' + '9')
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    while True:
        try:
            move = int(input(f"Input a number 1 to 9 to place {turn} in one of the nine squares: "))
            while theBoard[move] != ' ':
                try:
                    move = int(input(f"Input a number 1 to 9 to place {turn} in one of the nine squares: "))
                except ValueError:
                    continue
        except ValueError:
            continue
        break
    theBoard[move] = turn
    if i >= 4:
        check_win()
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
