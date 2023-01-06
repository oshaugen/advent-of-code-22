#! /usr/bin/python

import time

abc = 'abcdefghijklmnopqrstuvwxyz'.upper()


def my_function():
    with open('aoc6_data.txt', 'r') as f:
        data = f.readline()
    chars = [c for c in data.rstrip()]
    i = 4
    while True:
        last_four = chars[i-4:i]
        if len(set(last_four)) == 4:
            print("answer part 1:", i)
            break
        i += 1
    i = 14
    while True:
        last_four = chars[i-14:i]
        if len(set(last_four)) == 14:
            print("answer part 2:", i)
            return
        i += 1


if __name__ == "__main__":
    start = time.time()
    my_function()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))