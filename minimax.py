'''
    Creators: Andrew Kinchler & Isaiah Roh
    Date: 11/19/2019

    This is the file to implement our Minimax algorithm
'''

import math
import pygame



def minimax(current_depth, max_turn, combined_walls, grid_status):
    '''
        Removed max_depth if we want to add that back

        For every value,
            check to see if no more moves
                if so return value
            else
                for every other value
                    check to see if no more moves

    '''

    grid_status, get_another_turn = _set_all_slots(grid_status, combined_walls, max_turn)

    if _no_more_moves(combined_walls):
        return _calculate_score(grid_status), None, None
    else:
        for column in range(0, len(combined_walls)):
            if False in combined_walls[column]:
                row = combined_walls[column].index(False)
                combined_walls[column][row] = True
                break

        best_value = 0
        my_x_cord = row
        my_y_cord = column
        for column in range(len(combined_walls)):
            for row in range(int(len(combined_walls) / 2)):
                if not combined_walls[column][row]:
                    if get_another_turn:
                        value, x_cord, y_cord = minimax(current_depth, max_turn, combined_walls, grid_status)
                    else:
                        value, x_cord, y_cord = minimax(current_depth, not max_turn, combined_walls, grid_status)

                    # if not best_value:
                    #    best_value = value
                    #    best_x_cord = row
                    #    best_y_cord = column
                    if max_turn:
                        if value > best_value:
                            best_value = value
                            my_x_cord = x_cord
                            my_y_cord = y_cord
                    else:
                        if value < best_value:
                            best_value = value
                            my_x_cord = x_cord
                            my_y_cord = y_cord

        if _no_more_moves(combined_walls):
            return _calculate_score(grid_status), 0, 0
        else:
            return best_value, best_x_cord, best_y_cord


def _no_more_moves(combined_walls):
    for x_cord_list in range(0, len(combined_walls)):
        if False in combined_walls[x_cord_list]:
            return False
    return True


def _set_all_slots(grid_status, combined_walls, max_turn):
    get_another_turn = False

    for column in range(len(grid_status)):
        for row in range(len(grid_status)):
            if grid_status[column][row] != 0 or _get_number_of_walls(grid_status, combined_walls, column, row) < 4:
                continue

            get_another_turn = True
            if max_turn:
                grid_status[column][row] = 2
            else:
                grid_status[column][row] = 1

    return grid_status, get_another_turn


def _get_number_of_walls(grid_status, combined_walls, slot_column, slot_row):
    number_of_walls = 0

    # if right wall is set
    if slot_column == len(grid_status) - 1:
        number_of_walls += 1
    elif combined_walls[(slot_column * 2) + 2][slot_row]:
        number_of_walls += 1

    # if lower wall is set
    if slot_row == len(grid_status) - 1:
        number_of_walls += 1
    elif combined_walls[(slot_column * 2) + 1][slot_row + 1]:
        number_of_walls += 1

    # if left wall is set
    if combined_walls[slot_column * 2][slot_row]:
        number_of_walls += 1

    # if upper wall is set
    if combined_walls[(slot_column * 2) + 1][slot_row]:
        number_of_walls += 1

    return number_of_walls


def _calculate_score(grid_status):
    player_points = 0
    comp_points = 0

    for column in range(len(grid_status)):
        for row in range(len(grid_status)):
            if grid_status[column][row] == 1:
                player_points += 1
            else:
                comp_points += 1

    if player_points > comp_points:
        return -10
    elif comp_points > player_points:
        return 10
    else:
        return 0
