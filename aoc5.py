#! /usr/bin/python

import time

abc = 'abcdefghijklmnopqrstuvwxyz'.upper()

def do_move(stack, m, f, t):
    mint = int(m)
    fint = int(f)-1
    tint = int(t)-1
    new_delta = stack[fint][:mint][::-1]
    stack[tint] = new_delta + stack[tint]
    stack[fint] = stack[fint][mint:]
    return stack


def my_function():
    with open('aoc5_data.txt', 'r') as f:
        data = f.readlines()
    stack = [[] for _ in range(9)]
    for line in data:
        for idx, c in enumerate(line):
            if c in abc:
                stack[int((idx-1)/4)].append(c)
        if line.startswith(' 1   2   3   4'):
            break

    moves = []
    for line in data:
        if line.startswith('move'):
            moves.append(line.rstrip().replace('move', '').replace('from', '').replace('to', '').strip().split())

    for move in moves:
        m, f, t = move
        stack = do_move(stack, m, f, t)

    ans = ''
    for el in stack:
        ans += el[0]
    print("answer part 1:", ans)


def do_move2(stack, m, f, t):
    mint = int(m)
    fint = int(f)-1
    tint = int(t)-1
    #for i in range(int(m)):
    #    stack[fint]
    new_delta = stack[fint][:mint]#[::-1]
    stack[tint] = new_delta + stack[tint]
    stack[fint] = stack[fint][mint:]
    return stack


def my_function2():
    with open('aoc5_data.txt', 'r') as f:
        data = f.readlines()
    stack = [[] for _ in range(9)]
    for line in data:
        for idx, c in enumerate(line):
            if c in abc:
                stack[int((idx-1)/4)].append(c)
        if line.startswith(' 1   2   3   4'):
            break

    moves = []
    for line in data:
        if line.startswith('move'):
            moves.append(line.rstrip().replace('move', '').replace('from', '').replace('to', '').strip().split())

    for move in moves:
        m, f, t = move
        stack = do_move2(stack, m, f, t)

    ans = ''
    for el in stack:
        ans += el[0]
    print("answer part 2:", ans)


if __name__ == "__main__":
    start = time.time()
    my_function()
    my_function2()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


