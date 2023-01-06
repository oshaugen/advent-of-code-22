from time import sleep
import json
#import jsonlines
import time
import math
from tkinter import *


def get_stones(pa, pb):
    #pos = []
    if pa[0] == pb[0]:
        y1, y2 = min([pa[1], pb[1]]), max([pa[1], pb[1]])
        pos = [(pa[0], el) for el in range(y1, y2+1)]
    else:
        x1, x2 = min([pa[0], pb[0]]), max([pa[0], pb[0]])
        pos = [(el, pa[1]) for el in range(x1, x2 + 1)]
    #print('__________________')
    #print(pa, pb, pos)
    return pos


def part_1():
    with open('aocdata14.txt', 'r') as f:
        cmds = [el.rstrip() for el in f.readlines()]
    #print(cmds)
    min_x, max_x = 10000, 0
    max_y = 0
    lines = []
    for line in cmds:
        positions = [(int(el.split(',')[0]), int(el.split(',')[1])) for el in line.split(' -> ')]
        lines.append(positions)
        min_x = min(min([p[0] for p in positions]), min_x)
        max_x = max(max([p[0] for p in positions]), max_x)
        max_y = max(max([p[1] for p in positions]), max_y)
    #print(min_x, max_x, max_y)
    answer = 0
    x_row = ['.' for _ in range(min_x-5, max_x+5)]
    matrix = [x_row.copy() for _ in range(max_y+5)]
    fiveh_ref = 500-min_x + 2

    corrected_lines = []
    for line in lines:
        positions = [(p[0]-500+fiveh_ref, p[1]) for p in line]
        corrected_lines.append(positions)

    for line in corrected_lines:
        for idx_p in range(0, len(line)-1):
            stones = get_stones(line[idx_p], line[idx_p+1])
            for p in stones:
                p_row, p_col = p[1], p[0]
                matrix[p_row][p_col] = '#'

    matrix[0][fiveh_ref] = '+'

    last_sand_count = 0
    sand_count = -1
    while last_sand_count != sand_count:
        last_sand_count = sand_count
        temp_matrix = matrix.copy()
        sand_pos = (fiveh_ref, 0)
        sand_static = False
        while not sand_static:
            if matrix[sand_pos[1]+1][sand_pos[0]] == '.':
                matrix[sand_pos[1]][sand_pos[0]] = '.'
                sand_pos = (sand_pos[0], sand_pos[1]+1)
                matrix[sand_pos[1]][sand_pos[0]] = 'o'
            elif matrix[sand_pos[1]+1][sand_pos[0]-1] == '.':
                matrix[sand_pos[1]][sand_pos[0]] = '.'
                sand_pos = (sand_pos[0]-1, sand_pos[1]+1)
                matrix[sand_pos[1]][sand_pos[0]] = 'o'
            elif matrix[sand_pos[1]+1][sand_pos[0]+1] == '.':
                matrix[sand_pos[1]][sand_pos[0]] = '.'
                sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
                matrix[sand_pos[1]][sand_pos[0]] = 'o'
            else:
                sand_static = True
            if sand_pos[1] == len(matrix)-1 or sand_pos[0] == 0 or sand_pos[0] == len(matrix[0])-1:
                matrix[sand_pos[1]][sand_pos[0]] = '.'
                sand_static = True
            matrix[0][fiveh_ref] = '+'
        sand_count = 0
        for ela in matrix:
            for elb in ela:
                if elb == 'o':
                    sand_count += 1

    print('answer part 1', last_sand_count)


def part_2():
    with open('aocdata14.txt', 'r') as f:
    #with open('aocdata14_test.txt', 'r') as f:
        cmds = [el.rstrip() for el in f.readlines()]
    min_x, max_x = 10000, 0
    max_y = 0
    lines = []
    for line in cmds:
        positions = [(int(el.split(',')[0]), int(el.split(',')[1])) for el in line.split(' -> ')]
        lines.append(positions)
        min_x = min(min([p[0] for p in positions]), min_x)
        max_x = max(max([p[0] for p in positions]), max_x)
        max_y = max(max([p[1] for p in positions]), max_y)
    answer = 0
    x_row = ['.' for _ in range(min_x-1000, max_x+1000)]
    matrix = [x_row.copy() for _ in range(max_y+5)]
    fiveh_ref = 500-min_x + 1000

    corrected_lines = []
    for line in lines:
        positions = [(p[0]-500+fiveh_ref, p[1]) for p in line]
        corrected_lines.append(positions)

    corrected_lines.append([(0, max_y+2), (len(matrix[0])-1, max_y+2)])

    for line in corrected_lines:
        for idx_p in range(0, len(line)-1):
            stones = get_stones(line[idx_p], line[idx_p+1])
            for p in stones:
                p_row, p_col = p[1], p[0]
                matrix[p_row][p_col] = '#'

    matrix[0][fiveh_ref] = '+'

    last_sand_count = 0
    sand_count = -1
    while last_sand_count != sand_count:
        last_sand_count = sand_count
        #c += 1
        temp_matrix = matrix.copy()
        sand_pos = (fiveh_ref, 0)
        sand_static = False
        while not sand_static:
            if matrix[sand_pos[1]+1][sand_pos[0]] == '.':
                matrix[sand_pos[1]][sand_pos[0]] = '.'
                sand_pos = (sand_pos[0], sand_pos[1]+1)
                matrix[sand_pos[1]][sand_pos[0]] = 'o'
            elif matrix[sand_pos[1]+1][sand_pos[0]-1] == '.':
                matrix[sand_pos[1]][sand_pos[0]] = '.'
                sand_pos = (sand_pos[0]-1, sand_pos[1]+1)
                matrix[sand_pos[1]][sand_pos[0]] = 'o'
            elif matrix[sand_pos[1]+1][sand_pos[0]+1] == '.':
                matrix[sand_pos[1]][sand_pos[0]] = '.'
                sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
                matrix[sand_pos[1]][sand_pos[0]] = 'o'
            else:
                sand_static = True
            if sand_pos[1] == len(matrix)-1 or sand_pos[0] == 0 or sand_pos[0] == len(matrix[0])-1:
                matrix[sand_pos[1]][sand_pos[0]] = '.'
                sand_static = True
            matrix[0][fiveh_ref] = '+'
        sand_count = 0
        for ela in matrix:
            for elb in ela:
                if elb == 'o':
                    sand_count += 1
        if matrix[1][499-min_x+1000] == 'o' and matrix[1][500-min_x+1000] == 'o' and matrix[1][501-min_x+1000] == 'o':
            print("answer part 2", sand_count+1)
            return


if __name__ == '__main__':
    start = time.time()
    part_1()
    part_2()

    print('Finished in {} seconds'.format(round(time.time() - start, 1)))
