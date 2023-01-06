#! /usr/bin/python

import time
import math

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet = [c.lower() for c in ALPHABET]
alphabet_dict = {c.lower(): alphabet.index(c) for c in alphabet}
alphabet_dict['S'] = 0
alphabet_dict['E'] = 25
#print(alphabet_dict)
#exit()
s_pos = (0, 0)
e_pos = (0, 0)
matrix = []


def value(position):
    return alphabet_dict[matrix[position[0]][position[1]]]


def part_1():

    #with open('aoc12_data_test.txt', 'r') as f:
    with open('aoc12_data.txt', 'r') as f:
        data = f.read().splitlines()
    global matrix
    matrix = [list(el) for el in data]
    s_row = [matrix.index(el) for el in matrix if 'S' in el][0]
    s_col = [matrix[s_row].index(el) for el in matrix[s_row] if el=='S'][0]
    e_row = [matrix.index(el) for el in matrix if 'E' in el][0]
    e_col = [matrix[e_row].index(el) for el in matrix[e_row] if el=='E'][0]
    e_pos = (e_row, e_col)
    #print(matrix)
    found_pos = {(s_row, s_col): 0}
    for step_value in range(0, 10000):
        neigh = []
        current_pos = list(found_pos.keys()).copy()
        current_pos = [p for p in found_pos.keys() if found_pos[p]==step_value ]
        for poss in current_pos:
            r, c = poss
            current_val = value(poss)
            curr_neigh = [el for el in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if el[0] >= 0 and el[0] < len(matrix) and el[1] >= 0 and el[1] < len(matrix[0])]
            curr_neigh = [el for el in curr_neigh if value(el) <= current_val + 1 and el not in found_pos.keys()]
            neigh = neigh + curr_neigh
        for pn in neigh:
            found_pos[pn] = step_value + 1
        if e_pos in found_pos.keys():
            break
    print("answer part 1:", found_pos[e_pos])


def my_function(s, e_pos):
    found_pos = {s: 0}
    for step_value in range(0, 500):
        neigh = []
        current_pos = list(found_pos.keys()).copy()
        current_pos = [p for p in found_pos.keys() if found_pos[p]==step_value ]
        for poss in current_pos:
            r, c = poss
            current_val = value(poss)
            curr_neigh = [el for el in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if el[0] >= 0 and el[0] < len(matrix) and el[1] >= 0 and el[1] < len(matrix[0])]
            curr_neigh = [el for el in curr_neigh if value(el) <= current_val + 1 and el not in found_pos.keys()]
            neigh = neigh + curr_neigh
        for pn in neigh:
            found_pos[pn] = step_value + 1
        if e_pos in found_pos.keys():
            #print("breaking", found_pos[e_pos])
            return found_pos[e_pos]
    return 10000


def part_2():
    #with open('aoc12_data_test.txt', 'r') as f:
    with open('aoc12_data.txt', 'r') as f:
        data = f.read().splitlines()
    global matrix
    matrix = [list(el) for el in data]
    e_row = [matrix.index(el) for el in matrix if 'E' in el][0]
    e_col = [matrix[e_row].index(el) for el in matrix[e_row] if el == 'E'][0]

    e_pos = (e_row, e_col)
    a_positions = []
    for idr, row in enumerate(matrix):
        for idc, col in enumerate(row):
            if col == 'a' or col == 'S':
                a_positions.append((idr, idc))

    lowest = 100000
    for ida, ap in enumerate(a_positions):
        l = my_function(ap, e_pos)
        lowest = min(l, lowest)
        #if l < 1000:
        #    print(lowest, ida, len(a_positions), ida / len(a_positions) * 100, '%')

    print("answer part 2 lowest", lowest)



if __name__ == "__main__":
    start = time.time()
    part_1()
    part_2() # lazy solution...
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


