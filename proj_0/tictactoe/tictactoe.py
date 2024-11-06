"""
Tic Tac Toe Player
"""
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

    >>> b1 = initial_state()
    >>> player(b1)
    'X'
    >>> b2 = [[EMPTY, EMPTY, EMPTY], [EMPTY, "X", EMPTY], [EMPTY, EMPTY, EMPTY]]
    >>> player(b2)
    'O'
    >>> b3 = [["O", "X", "O"], [EMPTY, "X", EMPTY], ["X", EMPTY, "O"]]
    >>> player(b3)
    'O'
    >>> b4 = [["O", "X", "O"], ["X", "X", "O"], ["X", "X", "O"]]
    >>> player(b4)

    """
    if terminal(board):
        return None

    count_x = sum(cell == "X" for row in board for cell in row)
    count_o = sum(cell == "O" for row in board for cell in row)
    count_empty = sum(cell is None for row in board for cell in row)

    if count_empty == 9 or count_o >= count_x:
        return "X"
    return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    >>> b1 = initial_state()
    >>> action_set1 = actions(b1)
    >>> action_set1 == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    True
    >>> b2 = [[EMPTY, EMPTY, EMPTY], [EMPTY, "X", EMPTY], [EMPTY, EMPTY, EMPTY]]
    >>> action_set2 = actions(b2)
    >>> action_set2 == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}
    True
    >>> b3 = [["O", "X", "O"], [EMPTY, "X", EMPTY], ["X", EMPTY, "O"]]
    >>> action_set3 = actions(b3)
    >>> action_set3 == {(1, 0), (1, 2), (2, 1)}
    True
    >>> b4 = [["O", "X", "O"], ["X", "X", "O"], ["X", "X", "O"]]
    >>> action_set4 = actions(b4)
    >>> action_set4 == set()
    True
    """
    actions = {(i, j) for i in range(3) for j in range(3) if board[i][j] is None}
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    >>> b1 = initial_state()
    >>> result(b1, (1,1))
    [[None, None, None], [None, 'X', None], [None, None, None]]
    >>> b2 = [[EMPTY, EMPTY, EMPTY], [EMPTY, "X", EMPTY], [EMPTY, EMPTY, EMPTY]]
    >>> result(b2, (1,1))
    Traceback (most recent call last):
        ...
    Exception: Invalid action
    >>> b3 = [[EMPTY, EMPTY, EMPTY], [EMPTY, "X", EMPTY], [EMPTY, EMPTY, EMPTY]]
    >>> result(b3, (0,1))
    [[None, 'O', None], [None, 'X', None], [None, None, None]]
    >>> b3
    [[None, None, None], [None, 'X', None], [None, None, None]]
    >>> b4 = [["O", "X", "O"], ["X", "X", "O"], ["X", "X", "O"]]
    >>> result(b4, (1,1))
    Traceback (most recent call last):
        ...
    Exception: Invalid action
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    turn = player(board)
    updated_board = copy.deepcopy(board)
    updated_board[action[0]][action[1]] = turn
    return updated_board


def winner(board):
    """
    Returns the winner of the game, if there is one.

    >>> b1 = initial_state()
    >>> winner(b1)

    >>> b2 = [["O", "X", EMPTY], ["X", "X", "O"], ["X", EMPTY, EMPTY]]
    >>> winner(b2)

    >>> b3 = [["O", EMPTY, EMPTY], ["O", "X", EMPTY], ["O", "X", "X"]]
    >>> winner(b3)
    'O'
    >>> b4 = [["X", "O", "O"], ["X", "X", "O"], ["X", "X", "O"]]
    >>> winner(b4)
    'X'
    """
    if ["X", "X", "X"] in board or ["X", "X", "X"] in [list(col) for col in zip(*board)]:
        return "X"
    elif ["O", "O", "O"] in board or ["O", "O", "O"] in [list(col) for col in zip(*board)]:
        return "O"
    elif [board[i][i] for i in range(3)] == ["X", "X", "X"] or [board[i][2-i] for i in range(3)] == ["X", "X", "X"]:
        return "X"
    elif [board[i][i] for i in range(3)] == ["O", "O", "O"] or [board[i][2-i] for i in range(3)] == ["O", "O", "O"]:
        return "O"
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    >>> b1 = initial_state()
    >>> terminal(b1)
    False
    >>> b2 = [["O", "X", EMPTY], ["X", "X", "O"], ["X", EMPTY, EMPTY]]
    >>> terminal(b2)
    False
    >>> b3 = [["O", EMPTY, EMPTY], ["O", "X", EMPTY], ["O", "X", "X"]]
    >>> terminal(b3)
    True
    >>> b4 = [["X", "O", "O"], ["X", "X", "O"], ["X", "X", "O"]]
    >>> terminal(b4)
    True
    """
    empty_count = sum(cell is None for row in board for cell in row)
    game_winner = winner(board)
    return empty_count == 0 or game_winner is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    >>> b1 = [["O", EMPTY, EMPTY], ["O", "X", EMPTY], ["O", "X", "X"]]
    >>> utility(b1)
    -1
    >>> b2 = [["X", "O", "O"], ["X", "X", "O"], ["X", "X", "O"]]
    >>> utility(b2)
    1
    >>> b3 = [["O", "X", "X"], ["X", "X", "O"], ["O", "O", "X"]]
    >>> utility(b3)
    0
    """
    game_winner = winner(board)
    return {"X": 1, "O": -1}.get(game_winner, 0)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    >>> b3 = [["O", "X", EMPTY], ["X", "X", "O"], ["O", EMPTY, EMPTY]]
    >>> minimax(b3)

    """
    # if terminal(board):
    #     return None
    # utilitis = {}
    # for action in actions(board):
    #     while not terminal(current_stage):
    #         current_stage = result(current_stage, minimax(current_stage))
    #     final_utility = utility(current_stage)
    #     if final_utility in utilitis:
    #         utilitis[final_utility].append(action)
    #     else:
    #         utilitis[final_utility] = [action]
    #
    # curr_player = player(board)
    # if curr_player == "X":
    #     return utilitis[1][0] if 1 in utilitis else utilitis[0][0]
    # return utilitis[-1][0] if 1 in utilitis else utilitis[0][0]

    if terminal(board):
        return None
    utilities = []
    player_actions = list(actions(board))
    for action in player_actions:
        updated_board = result(board, action)

        while not terminal(updated_board):
            optimal_action = minimax(updated_board)
            updated_board = result(updated_board, optimal_action)

        final_utility = utility(updated_board)
        utilities.append(final_utility)

    # Utilities match action with its utility,
    # for use X, prefer to choose action with utility 1
    # for use O, prefer to choose action with utility -1

    curr_player = player(board)
    if curr_player == "X":
        mild_solution = None
        worst_solution = None
        for i in range(len(utilities)):
            if utilities[i] == 1:
                return player_actions[i]
            elif utilities[i] == 0:
                mild_solution = player_actions[i]
            else:
                worst_solution = player_actions[i]
        return mild_solution if mild_solution is not None else worst_solution
    else:
        mild_solution = None
        worst_solution = None
        for i in range(len(utilities)):
            if utilities[i] == -1:
                return player_actions[i]
            elif utilities[i] == 0:
                mild_solution = player_actions[i]
            else:
                worst_solution = player_actions[i]
        return mild_solution if mild_solution is not None else worst_solution

