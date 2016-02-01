"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui # CodeSkulptor Module
import poc_ttt_provided as provided # CodeSkulptor Module

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 10         # Number of trials to run. Increase for better accuracy.
SCORE_CURRENT = 1.0 # Score for squares played by the current player.
SCORE_OTHER = 1.0   # Score for squares played by the other player.
    
def mc_trial(board, player):
    """
    Takes a current board and the next player to move.
    Plays a game starting with the given player by making 
    random moves on the provided board, alternating between 
    players.
    """
    curr_player = player
    size = board.get_dim()
    # Keep playing until the game has ended.
    while (board.check_win() == None):
        next_row = random.randrange(size)
        next_col = random.randrange(size)
        # Ensure a move is being made to an empty square.
        while board.square(next_row, next_col) != provided.EMPTY:
            next_row = random.randrange(size)
            next_col = random.randrange(size)
        
        # Make the move.
        board.move(next_row, next_col, curr_player)
        # Switch players.
        curr_player = provided.switch_player(curr_player)

def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores with the same dimensions as the 
    Tic-Tac-Toe board, a board from a completed game, and 
    which player the machine player is. Updates the scores
    grid.
    """
    size = board.get_dim()
    winner = board.check_win()
    machine_won = winner == player
    for row in range(size):
        for col in range(size):
            # Get the current square.
            square = board.square(row, col)
            # Score is 0 for all squares in a DRAW or if the square is EMPTY.
            if winner == provided.DRAW or square == provided.EMPTY:
                scores[row][col] += 0
            # Add or subtract the appropriate score based on which player won.
            else:
                if square == player:
                    if machine_won:
                        scores[row][col] += SCORE_CURRENT
                    else:
                        scores[row][col] -= SCORE_CURRENT
                else:
                    if machine_won:
                        scores[row][col] -= SCORE_OTHER
                    else:
                        scores[row][col] += SCORE_OTHER                              

def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores. Finds all
    of the empty squares with the maximum score and randomly
    returns one of them as a (row, column) tuple.
    """
    moves = []
    max_scores = []
    size = board.get_dim()

    # Create a list of all the scores in the score grid.
    for row in range(size):
        for col in range(size):
            max_scores.append(scores[row][col])

    # Set the value of the list to be a 
    # reverse-sorted set of the scores.
    max_scores = sorted(set(max_scores), reverse=True)

    # Find all empty squares with the max score and build a list.
    while len(moves) == 0:
        max_score = max_scores[0]
        for row in range(size):
            for col in range(size):
                if scores[row][col] == max_score and board.square(row, col) == provided.EMPTY:
                    moves.append((row, col))
        # Done looking for moves with this score, now look for next highest.
        max_scores.pop(0)

    # Select a random row, col tuple from the list of moves and return it.
    rand_move = random.randrange(len(moves))
    return moves[rand_move]

def mc_move(board, player, trials):
    """
    Takes the current board, which player the machine player
    is, and the number of trials to run. Returns a move for
    the machine player in the form of a (row, column) tuple.
    """
    board_size = board.get_dim()
    scores = [[0 for dummy in range(board_size)] for dummy in range(board_size)]
    for dummy in range(trials):
        mc_board = board.clone()
        mc_trial(mc_board, player)
        mc_update_scores(scores, mc_board, player)
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
