# Write a method that takes a field for well-known board game "Battleship" as an
# argument and returns true if it has a valid disposition of ships, false otherwise.
# Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers,
# 0 if the cell is free and 1 if occupied by ship.
#
# Battleship (also Battleships or Sea Battle) is a guessing game for two players.
# Each player has a 10x10 grid containing several "ships" and objective is to destroy
# enemy's forces by targetting individual cells on his field. The ship occupies one or
# more cells in the grid. Size and number of ships may differ from version to version.
# In this kata we will use Soviet/Russian version of the game.
#
#
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3),
# 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.
#
# The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
#
# This is all you need to solve this kata.
# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

random_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

random_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]]

random_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0]]


def check_1_s(field: list, count: int) -> bool:
    if sum(x.count(1) for x in field) != count:
        return False
    return True


def fill_zeros(field: list, start: tuple, ship: int, hor: bool) -> None:
    dir_h, dir_v = (1, 0) if hor else (0, 1)
    fill_v_start = max(start[0] - 1, 0)
    fill_v_end = min(start[0] + 1 + dir_v * (ship - 1), 9)
    fill_h_start = max(start[1] - 1, 0)
    fill_h_end = min(start[1] + 1 + dir_h * (ship - 1), 9)
    fill_len = fill_h_end - fill_h_start
    for row in range(fill_v_start, fill_v_end+1):
        field[row][fill_h_start:fill_h_end] = [0 for _ in range(fill_len)]
    return

def identify_ship(field: list, start: tuple) -> (int, bool):
    if start[0] == start[1] == 9:
        return 1, True
    ship_size = 1
    h_lim = min(start[1] + 4, 9)
    v_lim = min(start[0] + 4, 9)
    v_dir = field[min(start[0] + 1, 9)][start[1]]
    h_dir = field[start[0]][min(start[1] + 1, 9)]
    if v_dir == h_dir == 0:
        return 1, True

    row, col = start
    it_start = v_dir*start[0] + h_dir * start[1]
    it_end = v_dir*v_lim + h_dir*h_lim
    for i in range(it_start, it_end+1):
        if field[row + v_dir * ship_size][col + h_dir * ship_size] == 0:
            return ship_size, bool(h_dir)
        ship_size += 1

    return ship_size, bool(h_dir)

def validate_battlefield(field: list) -> bool:
    budget = [None, 4, 3, 2, 1]
    num_ones = 20
    if not check_1_s(field, num_ones):
        return False
    for x in range(10):
        for y in range(10):
            if field[x][y] == 1:
                size, hor = identify_ship(field, (x, y))
                if size == 0:
                    return False
                if budget[size] == 0:
                    return False
                budget[size] -= 1
                fill_zeros(field, (x, y), size, hor)
                num_ones -= size
        if not check_1_s(field, num_ones):
            return False
    return True

assert validate_battlefield(random_1) == True
print(random_1)
assert validate_battlefield(random_2) == True
print(random_2)
assert validate_battlefield(random_3) == True
print(random_3)

