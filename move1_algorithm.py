import random

def remove_from_list():
    moves = ["1-Left", "2-Right", "3-Up", "4-Down", "5-Jump", "6-Crouch"]
    move_list = moves.copy()

    while move_list:
        selected_move = random.choice(move_list)
        print(f"Selected move: {selected_move}")
        move_list.remove(selected_move)




remove_from_list()