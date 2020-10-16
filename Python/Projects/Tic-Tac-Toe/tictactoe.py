"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_of_X = count_of_O=0
    for row in board:
         for entry in row:
             if entry == X:
                 count_of_X= count_of_X + 1
             elif entry==O:
                 count_of_O = count_of_O + 1
    
    if count_of_O==count_of_X:
        turn= X
    if count_of_X>count_of_O:
        turn = O
    if count_of_X<count_of_O:
        turn= X
    return turn
        



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set= set()
    for row_no,row in enumerate(board):
        for cell_no,entry in enumerate(row):
            if entry== EMPTY:
                actions_set.add((row_no,cell_no))
    return actions_set            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is not None:
        i = action[0]
        j= action[1]
        if board[i][j]!= EMPTY:
          raise Exception("Invalid Action")
        turn = player(board)
        board_copy = copy.deepcopy(board)
        board_copy[i][j] = turn
        return board_copy
    else:
        raise Exception("Some fuckup")



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        value= utility(board)
        if(value==1):
            return X
        elif(value== -1):
            return O
    #no winner when terminal state is false or when it's a stalemate        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #check if all places are filled 
    # simoultaneoly check if any of the rows contain 3 consective X's or O's
    count_of_EMPTY= 0
    for row in board:
        X_row_count = O_row_count=0
        for entry in row:
            if entry == EMPTY:
                count_of_EMPTY= count_of_EMPTY +1
            elif entry== X:
                X_row_count = X_row_count +1
            else:
                O_row_count = O_row_count +1
        if(X_row_count==3 or O_row_count==3 ):
            return True    
    
    if count_of_EMPTY==0:
        return True
    
    #check if any column contains consective X's or O's
    for i in range(3):
        X_column_count = O_column_count =0
        for j in range(3):
            if board[j][i]== X :
                X_column_count= X_column_count +1
            elif board[j][i]== O:
                O_column_count = O_column_count +1
        if(O_column_count==3 or X_column_count==3):
            return True

     #finally check diagonals
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]

    X_diagonal_count = O_diagonal_count = 0
    for element in diagonal_1:
         if element == X:
             X_diagonal_count = X_diagonal_count +1
         elif element == O:
             O_diagonal_count = O_diagonal_count +1
    if(X_diagonal_count==3 or O_diagonal_count==3):
            return True

    X_diagonal_count = O_diagonal_count = 0
    for element in diagonal_2:
         if element == X:
             X_diagonal_count = X_diagonal_count +1
         elif element == O:
             O_diagonal_count = O_diagonal_count +1
    if(X_diagonal_count==3 or O_diagonal_count==3):
            return True   
    return False            



    

                             
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
     #check if all places are filled 
    # simoultaneoly check if any of the rows contain 3 consective X's or O's
    for row in board:
        X_row_count = O_row_count=0
        for entry in row:
            if entry== X:
                X_row_count = X_row_count +1
            else:
                O_row_count = O_row_count +1
        if(X_row_count==3):
            return 1
        if(O_row_count==3):
            return -1    
    
    #check if any column contains consective X's or O's
    for i in range(3):
        X_column_count = O_column_count =0
        for j in range(3):
            if board[j][i]== X :
                X_column_count= X_column_count +1
            elif board[j][i]== O:
                O_column_count = O_column_count +1
        if(O_column_count==3):
            return -1
        if(X_column_count==3):
            return 1

     #finally check diagonals
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]

    X_diagonal_count = O_diagonal_count = 0
    for element in diagonal_1:
         if element == X:
             X_diagonal_count = X_diagonal_count +1
         elif element == O:
             O_diagonal_count = O_diagonal_count +1
    if(X_diagonal_count==3):
            return 1
    if(O_diagonal_count==3):
         return -1

    X_diagonal_count = O_diagonal_count = 0
    for element in diagonal_2:
         if element == X:
             X_diagonal_count = X_diagonal_count +1
         elif element == O:
             O_diagonal_count = O_diagonal_count +1
    if(X_diagonal_count==3):
            return 1
    if(O_diagonal_count==3):
         return -1  


    return 0     

    #returns best possible action for min player
def MIN_VALUE(board):
    if terminal(board):
        return (utility(board),None)


    v= 10000
    for action in actions(board):
        current_value = MAX_VALUE(result(board,action))
        if current_value[0] == -1:
            return (-1,action)
        if v> (current_value[0]):
            v= current_value[0]
            move= action
        
    return(v,move)


        #returns best possible solution for max player
def MAX_VALUE(board):
    if terminal(board):
        return (utility(board),None)

    v= -100000
    for action in actions(board):
        current_value = MIN_VALUE(result(board,action))
        if current_value[0] == 1:
            return (1,action)
        if v<current_value[0]:
            v= current_value[0]
            move= action
        
        return(v,move)
 



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #if board is in terminal state return none
    if terminal(board):
        return None
    turn = player(board)
    if(turn==X):
        return (MAX_VALUE(board)[1])
    elif(turn==O):
        return (MIN_VALUE(board)[1])


        
