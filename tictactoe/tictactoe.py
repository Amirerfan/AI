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
    flag = 0

    for row in board:
        for position in row:
            if (position == X):
                flag += 1
            elif (position == O):
                flag -= 1

    if (flag > 0):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for row in range(3):
        for column in range(3):
            if (board[row][column] == EMPTY):
                actions.append((row, column))
    
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    temp_board = copy.deepcopy(board)
    temp_board[action[0]][action[1]] = player(board)

    return  temp_board
    

def winner_name(player):
    if (player == X):
        return X
    else:
        return O


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    temp_borad = []

    # Create Temp Board
    for row in board:
        temp_borad += row

    for i in range(3):
        # Check Column 
        if ((temp_borad[i] == temp_borad[i+3]) and (temp_borad[i] == temp_borad[i+6])):
            if (temp_borad[i] != EMPTY):
                return winner_name(temp_borad[i])
                    
        # Check Row
        if (temp_borad[i*3] == temp_borad[i*3+1] and temp_borad[i*3] == temp_borad[i*3+2]):
            if (temp_borad[i*3] != EMPTY):
                return winner_name(temp_borad[i*3])

    if (temp_borad[0] == temp_borad[4] and temp_borad[0] == temp_borad[8]):
        if (temp_borad[0] != EMPTY):
            return winner_name(temp_borad[0])
    
    if (temp_borad[2] == temp_borad[4] and temp_borad[2] == temp_borad[6]):
        if (temp_borad[2] != EMPTY):
            return winner_name(temp_borad[2])

    return None
    
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True
    else:
        if (len(actions(board))):
            return False
        else:
            return True


def score(player):
    if(player == X):
        return 1
    else:
        return -1


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    temp_borad = []

    # Create Temp Board
    for row in board:
        temp_borad += row

    for i in range(3):

        # Check Column 
        if (temp_borad[i] == temp_borad[i+3] and temp_borad[i] == temp_borad[i+6]):
            if (temp_borad[i] != EMPTY):
                return score(temp_borad[i])
                    
        # Check Row
        if (temp_borad[i*3] == temp_borad[i*3+1] and temp_borad[i*3] == temp_borad[i*3+2]):
            if (temp_borad[i*3] != EMPTY):
                return score(temp_borad[i*3])

    if (temp_borad[0] == temp_borad[4] and temp_borad[0] == temp_borad[8]):
        if (temp_borad[0] != EMPTY):
            return score(temp_borad[0])
    
    if (temp_borad[2] == temp_borad[4] and temp_borad[2] == temp_borad[6]):
        if (temp_borad[2] != EMPTY):
            return score(temp_borad[2])
    
    return 0


def min_value(board):
    
    if (terminal(board)):
        return utility(board), None

    value = math.inf

    for action in actions(board):
        new_value = min(value, max_value(result(board, action))[0])
        if (new_value < value):
            best_action = action
            value = new_value

    return value, best_action


def max_value(board):

    if (terminal(board)):
        return utility(board), None

    value = - math.inf

    for action in actions(board):
        new_value = max(value, min_value(result(board, action))[0])
        if (new_value > value):
            best_action = action
            value = new_value

    return value, best_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (player(board) == X):
        return max_value(board)[1]     
    else:
        return min_value(board)[1]
