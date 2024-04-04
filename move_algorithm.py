import random

# Moves dictionary
moves = {
    1: 'left',
    2: 'right',
    3: 'up',
    4: 'down',
    5: 'jump',
    6: 'crouch'
}

# Initialize the list of moves from the dictionary
moves_list = list(moves.values())

# The algorithm will run until all moves are removed from the list
while moves_list:
    # Randomly pick a move from the list
    move = random.choice(moves_list)
    print(move)
    # Remove the chosen move from the list
    moves_list.remove(move)