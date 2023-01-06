#! /usr/bin/python

import time


def my_function():
    with open('aoc4_data.txt', 'r') as f:
        data = f.readlines()
    data = [el.rstrip().split(',') for el in data]
    c1, c2 = 0, 0
    for pair in data:
        s1 = set([el for el in range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1])+1)])
        s2 = set([el for el in range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1])+1)])

        if max(len(s1), len(s2)) == len(set(list(s1)+list(s2))):
            c1 += 1
        if len(s1) + len(s2) > len(set(list(s1)+list(s2))):
            c2 += 1
    print("answer part 1:", c1)
    print("answer part 2:", c2)


def my_function2():
    with open('aoc3_data.txt', 'r') as f:
        data = f.readlines()
    res = []
    for el in data:
        r = set(list(el.rstrip()))
        res.append(r)
    badges = []
    while res:
        r1 = res.pop(0)
        r2 = res.pop(0)
        r3 = res.pop(0)
        inter_temp = [el for el in r1 if el in r2]
        inter = [el for el in r3 if el in inter_temp]
        badges += inter
    print(badges)
    abc = 'abcdefghijklmnopqrstuvwxyz'
    # (#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    abc += abc.upper()
    sum = 0
    for c in badges:
        sum += abc.index(c) + 1
        print(c, abc.index(c) + 1)
    print(sum)

if __name__ == "__main__":
    start = time.time()
    my_function()
    #my_function2()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


