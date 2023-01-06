#! /usr/bin/python

import time


def my_function():
    with open('aoc3_data.txt', 'r') as f:
        data = f.readlines()
    res = []
    for el in data:
        num = int(len(el)/2)
        #print(num)
        r1, r2 = set(list(el[:num])), set(list(el.rstrip()[num:]))
        inters = [a for a in r1 if a in r2]
        #print("inters", inters)
        res += inters
    abc = 'abcdefghijklmnopqrstuvwxyz'
    #(#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    abc += abc.upper()
    sum = 0
    for c in res:
        sum += abc.index(c) + 1
    print("answer part 1:", sum)


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
    # print(badges)
    abc = 'abcdefghijklmnopqrstuvwxyz'
    # (#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    abc += abc.upper()
    sum = 0
    for c in badges:
        sum += abc.index(c) + 1
        # print(c, abc.index(c) + 1)
    print("answer part 2:", sum)

if __name__ == "__main__":
    start = time.time()
    my_function()
    my_function2()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


