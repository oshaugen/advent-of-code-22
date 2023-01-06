#! /usr/bin/python

import time

m_list = [0 for el in range(10)]
n_list = [0 for el in range(10)]
s_list = [0 for el in range(10)]


def my_function():
    with open('aoc1_data.txt', 'r') as f:
        data = f.readlines()
    groups = []
    temp_sum = 0
    for el in data:
        if el == '\n':
            groups.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(el.rstrip())
    print(groups)
    print("answer part 1:", max(groups))
    sorted_groups = sorted(groups, reverse=True)
    print("answer part 2:", sum(sorted_groups[0:3]))


if __name__ == "__main__":
    start = time.time()
    my_function()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


