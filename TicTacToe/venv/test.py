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
    # X always starts if board is empty
    if board == initial_state():
        return X

    x_count=0
    o_count=0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    # X always starts the game. Always ahead after playing turn.
    if(x_count > o_count):
        return O
    # O always equalizes after playing turn.
    elif(x_count == o_count):
        return X




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action_set.add((i,j))

    return action_set



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action[0] not in range(3) or action[1] not in range(3):
        raise Exception("Invalid action")


    updated_board = copy.deepcopy(board)

    if player(board) == X:
        updated_board[action[0]][action[1]] = X

    elif player(board) == O:
        updated_board[action[0]][action[1]] = O

    #returning updated board
    return updated_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #ROW CHECK:

    for i in range(len(board)):
        if board[i]== [X,X,X]:
            return X
        elif board[i] == [O,O,O]:
            return O

    #COLUMN CHECK:

    #(transposing board):
    trans_board = [[EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY]]

    for i in range(len(board)):
        for j in range(len(board[0])):
            trans_board[j][i] = board[i][j]

    #(running same test):
    for i in range(len(board)):
        if trans_board[i]== [X,X,X]:
            return X
        elif trans_board[i] == [O,O,O]:
            return O

    #DIAGONALS CHECK:

    r_diag = [board[0][2], board[1][1], board[2][0]]
    l_diag = [board[0][0], board[1][1], board[2][2]]

    if r_diag == [X,X,X] or l_diag == [X,X,X]:
        return X
    elif r_diag == [O,O,O] or l_diag == [O,O,O]:
        return O


    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False

    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board)== X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) is None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    turn = player(board)
    bestAction = ()

    if turn == X:

        bestVal = -math.inf

        for action in actions(board):
            val = minVal(result(board,action))
            if val > bestVal:
                bestVal = val
                bestAction = action
        return bestAction

    elif turn == O:

        bestVal = math.inf

        for action in actions(board):
            val = maxVal(result(board, action))
            if val < bestVal:
                bestVal = val
                bestAction = action
        return bestAction

def maxVal(board):
    if terminal(board):
        return utility(board)
    val = -math.inf

    for action in actions(board):
        val = max(val, minVal(result(board,action)))
    return val

def minVal(board):
    if terminal(board):
        return utility(board)
    val = math.inf

    for action in actions(board):
        val = min(val, maxVal(result(board, action)))
    return val