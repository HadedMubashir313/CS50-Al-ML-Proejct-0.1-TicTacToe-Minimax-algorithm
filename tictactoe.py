"""
Tic Tac Toe Player
"""

import math

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
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    return X if x_count == o_count else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action

    if board[i][j] != EMPTY:
        raise Exception ("invalid action, cell already occupied")
    import copy
    new_board = copy.deepcopy(board)

    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0]!= EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]!= EMPTY:
            return board[0][col]
    if board[0][0] == board [1][1] == board[2][2] and board[0][0]!= EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!= None:
        return True
    
    if len(actions(board))==0:
        return True
    
    return False
           

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)== X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X wants to maximize
        v = -math.inf
        best_action = None
        
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > v: #0 / 1 
                v = min_val
                #If min_val < v, then nothing happens - we just skip it and try the next action.
                best_action = action

        
        return best_action
    
    else:
        # O wants to minimize
        v = math.inf
        best_action = None
        
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_action = action
        
        return best_action

def max_value(board):
    """Helper function: returns the maximum value for X"""
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v

def min_value(board):
    """Helper function: returns the minimum value for O"""
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v

