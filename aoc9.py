#! /usr/bin/python

import time
#import math
#import numpy as np


def get_tail_pos(h, t):
    if abs(h[0] - t[0]) >= 2 and h[1] == t[1]:
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1
    elif abs(h[1] - t[1]) >= 2 and h[0] == t[0]:
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1
    elif abs(h[0] - t[0]) >= 2 and abs(h[1] - t[1]) == 1:
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1
        t[1] = h[1]
    elif abs(h[1] - t[1]) >= 2 and abs(h[0] - t[0]) == 1:
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1
        t[0] = h[0]
    elif abs(h[0] - t[0]) >= 2 and abs(h[1] - t[1]) >= 2:
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1

    return t.copy()


def my_function():
    #with open('aoc9_data_test2.txt', 'r') as f:
    with open('aoc9_data.txt', 'r') as f:
        moves = f.read().splitlines()
    rows = []
    #h = [0, 0]#, [0, 0]
    tails = [[0, 0] for _ in range(0, 10)]
    directions = {'R':(0, 1), 'L':(0, -1), 'U':(-1, 0), 'D':(1, 0)}
    t_pos = []
    for l in moves:
        direction, steps = l.split(' ')[0], int(l.split(' ')[1])
        for _ in range(steps):
            tails[0] = [tails[0][0] + directions[direction][0], tails[0][1] + directions[direction][1]]
            for i in range(1, 10):
                tails[i] = get_tail_pos(tails[i-1], tails[i])
                #if l == 'D 3':
                #    print(l, tails)


            t_pos.append(tails[-1].copy())
        #print("____________________")
    print(len(t_pos))
    unique_pos = [list(x) for x in set(tuple(x) for x in t_pos)]
    #print(unique_pos)
    print("answer:", len(unique_pos))


if __name__ == "__main__":
    start = time.time()
    my_function()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


