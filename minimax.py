'''
    Creators: Andrew Kinchler & Isaiah Roh
    Date: 11/19/2019

    This is the file to implement our Minimax algorithm
'''

import math


def minimax(current_depth, max_depth, max_turn, combined_walls):
    '''
        if no more moves or hit max depth
            then return heuristic value

        for each possible move
            make it and call minimax
            return max or min
    '''

    if current_depth == max_depth or _no_more_moves():
        return _calculate_score(combined_walls), None, None
    else:
        for x_cord in range(0, len(combined_walls)):
            if False in combined_walls[x_cord]:
                y_cord = combined_walls[x_cord].index(False)
                break
        combined_walls[x_cord][y_cord] = True

        # Need to change
        if max_turn:
            return max(minimax(current_depth + 1, node_index * 2, False, scores, target_depth),
                       minimax(current_depth + 1, node_index * 2 + 1, False, scores, target_depth))
        else:
            return min(minimax(current_depth + 1, node_index * 2, True, scores, target_depth),
                       minimax(current_depth + 1, node_index * 2 + 1, True, scores, target_depth))


def _no_more_moves(combined_walls):
    if False in combined_walls:
        return False
    else:
        return True


def _calculate_score(combined_walls):
    # return value to send back
    pass
