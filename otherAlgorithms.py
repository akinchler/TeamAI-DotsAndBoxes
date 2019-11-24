'''
    Creators: Andrew Kinchler
    Date: 11/19/2019

    This is the file to implement other base algorithms to test against
'''

import random


def pick_randomly(walls, grid_size):
    searching_for_open_wall = True
    while searching_for_open_wall:
        column = random.randint(1, (grid_size * 2) - 1)
        row = random.randint(0, grid_size - 1)

        if not walls[column][row]:
            searching_for_open_wall = False
    cords = [column, row]
    return cords
