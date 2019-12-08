

import numpy as np
import copy
import time
import minimax
import otherAlgorithms
import random
import csv

RESULTS = [['Grid Size', 'Opponent', 'Went First', 'Max Depth', 'Total Turns', 'Minimax Turns', 'Avg Turn Time', 'Max Turn Time',
            'Total Turn Time', 'Minimax Points', 'Opponent Points', 'Winner']]


def run_game(i_grid_size, i_algorithm, i_max_depth):
    grid_size = i_grid_size
    algorithm = i_algorithm  # 1 = random, 2 = greedy, 3 = defensive
    max_depth = i_max_depth

    a_boxes = 0
    b_boxes = 0
    boxes = np.zeros((grid_size, grid_size), np.int)
    walls = np.zeros((grid_size * 2, grid_size), np.dtype(bool))

    for column in range(grid_size * 2):
        for row in range(grid_size):
            if column == 0 or (column % 2 == 1 and row == 0):
                walls[column][row] = True

    if random.randint(1, 2) == 1:
        turn = 'A'
        starting = 'Minimax'
    else:
        turn = 'B'
        starting = 'Opponent'

    total_turns = 0
    minimax_turns = 0
    all_turn_times = []
    my_box = [-100, -100]
    game_over = False

    while not game_over:
        total_turns += 1
        column = 0
        row = 0

        if turn == 'A':
            minimax_turns += 1
            boxes_copy = copy.copy(boxes)
            walls_copy = copy.copy(walls)
            start = time.time()
            node = minimax.Node('A', max_depth, boxes_copy, walls_copy)
            best_value, best_cords = minimax.min_max(node)
            turn_time = time.time() - start
            all_turn_times.append(turn_time)
            column = best_cords[0]
            row = best_cords[1]

        if turn == 'B':
            cords = []

            if algorithm == 1:
                cords = otherAlgorithms.pick_randomly(walls, grid_size)
            elif algorithm == 2:
                cords, my_box = otherAlgorithms.greedy_algorithm(walls, boxes, my_box)
            elif algorithm == 3:
                cords = otherAlgorithms.defensive_algorithm(walls, boxes)
            else:
                exit(1)

            column = cords[0]
            row = cords[1]

        walls[column][row] = True

        boxes, get_another_turn, a_boxes, b_boxes = _set_all_slots(boxes, walls, turn, a_boxes, b_boxes)

        if not get_another_turn:
            if turn == "A":
                turn = "B"
            elif turn == "B":
                turn = "A"

        if a_boxes + b_boxes == grid_size ** 2:
            game_over = True

        if game_over:

            if a_boxes == b_boxes:
                winner = 'Tie'
            elif a_boxes > b_boxes:
                winner = 'Minimax'
            else:
                winner = 'Opponent'

            total_time = 0
            for round_trip in all_turn_times:
                total_time += round_trip
            average_time = total_time / len(all_turn_times)

            if algorithm == 1:
                opponent = 'Random'
            elif algorithm == 2:
                opponent = 'Greedy'
            else:
                opponent = 'Defensive'

            result = [grid_size, opponent, starting, max_depth, total_turns, minimax_turns, average_time,
                      max(all_turn_times), total_time, a_boxes, b_boxes, winner]
            RESULTS.append(result)


def _set_all_slots(boxes, walls, player, a_boxes, b_boxes):
    get_another_turn = False

    for column in range(len(boxes)):
        for row in range(len(boxes)):
            if boxes[column][row] != 0 or _get_number_of_walls(boxes, walls, column, row) < 4:
                continue

            get_another_turn = True
            if player == 'A':
                boxes[column][row] = 1
                a_boxes += 1
            elif player == 'B':
                boxes[column][row] = 2
                b_boxes += 1
            else:
                boxes[column][row] = 3

    return boxes, get_another_turn, a_boxes, b_boxes


def _get_number_of_walls(boxes, walls, slot_column, slot_row):
    number_of_walls = 0

    # if right wall is set
    if slot_column == len(boxes) - 1:
        number_of_walls += 1
    elif walls[(slot_column * 2) + 2][slot_row]:
        number_of_walls += 1

    # if lower wall is set
    if slot_row == len(boxes) - 1:
        number_of_walls += 1
    elif walls[(slot_column * 2) + 1][slot_row + 1]:
        number_of_walls += 1

    # if left wall is set
    if walls[slot_column * 2][slot_row]:
        number_of_walls += 1

    # if upper wall is set
    if walls[(slot_column * 2) + 1][slot_row]:
        number_of_walls += 1

    return number_of_walls


if __name__ == '__main__':
    # Random
    for i in range(100):
        print('Starting Random game:', i)
        run_game(5, 1, 3)

    # Greedy
    for i in range(100):
        print('Starting Greedy game:', i)
        run_game(5, 2, 3)

    # Defensive
    for i in range(100):
        print('Starting Defensive game:', i)
        run_game(5, 3, 3)

    with open('output.csv', 'w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerows(RESULTS)
