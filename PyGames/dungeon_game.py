import random
import os


# draw grid
# pick random location for the player
# pick random location for the exit door
# pick random location for the monster
# draw a player in the grid
# take input or movement
# move player, unless invalid move (past edges of grid)
# check for win/lose
# clear screen and random grid


CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player

    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1

    return x, y


def get_move(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    x, y = player

    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")

    return moves


def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_move(player)
        print("you're currently in room {}".format(player))
        print("you can move {}".format(", ".join(valid_moves)))
        print("Enter `QUIT` to quit.")

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            break

        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n ** OH NO! The monster got you! Better luck next time! ** \n")
                playing = False
            if player == door:
                print("\n ** You scaped! Congratulation general ** \n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! ** \n")
    else:
        if input('Play again? [Y/n] ').lower() != "n":
            game_loop()


clear_screen()
print("welcom to the dungeon!")
input("press `return` to start!")
clear_screen()
game_loop()
