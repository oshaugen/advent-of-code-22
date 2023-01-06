#! /usr/bin/python

import time

m_list = [0 for el in range(10)]
n_list = [0 for el in range(10)]
s_list = [0 for el in range(10)]

 # a x rock 1
 # b y paper 2
 # c z scissor 3

def my_function():
    with open('aoc2_data.txt', 'r') as f:
        data = f.readlines()
    rps = []
    for el in data:
        rps.append((el.rstrip().split()))
    #print(rps)
    psum, p = 0, 0
    for el in rps:
        if el[0] == 'A':
            if el[1] == 'X':
                p = 1+3
            elif el[1] == 'Y':
                p = 2+6
            elif el[1] == 'Z':
                p = 3+0
        elif el[0] == 'B':
            if el[1] == 'X':
                p = 1+0
            elif el[1] == 'Y':
                p = 2+3
            elif el[1] == 'Z':
                p = 3+6
        elif el[0] == 'C':
            if el[1] == 'X':
                p = 1+6
            elif el[1] == 'Y':
                p = 2+0
            elif el[1] == 'Z':
                p = 3+3
        psum += p
    print("answer part 1:", psum)

def my_function2():
    # a  rock 1
    # b  paper 2
    # c  scissor 3
    # x loose
    # y draw
    # z win
    with open('aoc2_data.txt', 'r') as f:
        data = f.readlines()
    rps = []
    for el in data:
        rps.append((el.rstrip().split()))
    #print(rps)

    psum, p = 0, 0
    for el in rps:
        if el[0] == 'A':
            if el[1] == 'X':
                # loose, scissor
                p = 3+0
            elif el[1] == 'Y':
                # draw rock
                p = 1+3
            elif el[1] == 'Z':
                p = 2+6
        elif el[0] == 'B':
            if el[1] == 'X':
                # loose rock
                p = 1+0
            elif el[1] == 'Y':
                # draw paper
                p = 2+3
            elif el[1] == 'Z':
                # win scissor
                p = 3+6
        elif el[0] == 'C':
            if el[1] == 'X':
                # loose paper
                p = 2+0
            elif el[1] == 'Y':
                # draw scissor
                p = 3+3
            elif el[1] == 'Z':
                # win rock
                p = 1+6
        psum += p
    print("answer part 2:", psum)

if __name__ == "__main__":
    start = time.time()
    my_function()
    my_function2()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


