#! /usr/bin/python

import time
import math


class Monkey:

    # The init method or constructor
    def __init__(self, number, items, operation, test, true_throw, false_throw):
        # Instance Variable
        #self.breed = breed
        #self.color = color
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspections = 0


def my_function2():

    with open('aoc11_data.txt', 'r') as f:
    #with open('aoc11_data_test.txt', 'r') as f:
        data = f.read().splitlines()

    data.append('')
    monkeys = []
    for line in data:
        if line.startswith('Monkey '):
            n = int(line.split(' ')[1].replace(':', ''))
        elif line.startswith('  Starting items: '):
            items = [int(el) for el in line.strip().replace(',','').split(' ') if el.isnumeric()]
        elif line.startswith('  Operation: new = old '):
            operation = line.replace('  Operation: new = old ', '')
        elif line.startswith('  Test: divisible by '):
            test = int(line.replace('  Test: divisible by ', ''))
        elif line.startswith('    If true: throw to monkey '):
            true_throw = int(line.replace('    If true: throw to monkey ', ''))
        elif line.startswith('    If false: throw to monkey '):
            false_throw = int(line.replace('    If false: throw to monkey ', ''))
        elif line == '':
            monkeys.append(Monkey(number=n, items=items, operation=operation, test=test, true_throw=true_throw, false_throw=false_throw))

    tests = 1
    for monk in monkeys:
        # print(monk.__dict__)
        tests = tests * monk.test

    for r in range(1, 10001):
        # if r%10 == 0:
        #    print("round: ", r)
        for m in monkeys:
            m.inspections += len(m.items)
            for item in m.items:
                if m.operation == '* old':
                    new_item = item*item
                elif m.operation.startswith('*'):
                    new_item = item * int(m.operation.replace('* ', ''))
                elif m.operation.startswith('+'):
                    new_item = item + int(m.operation.replace('+ ', ''))
                #print(m.number, item, new_item)
                #new_item = math.floor(new_item/3)
                #print(m.number, item, new_item)
                #while new_item > 3*tests:
                #    new_item = new_item - tests
                modulo = math.floor(new_item / tests)
                new_item = new_item - modulo*tests
                #print(m.number, item, new_item)
                if new_item % m.test == 0:
                    monkeys[m.true_throw].items.append(new_item)
                    #print(monkeys[m.true_throw].__dict__)
                else:
                    monkeys[m.false_throw].items.append(new_item)
                    #print(monkeys[m.false_throw].__dict__)
            m.items = []

    inspections = sorted([m.inspections for m in monkeys], reverse=True)
    print("answer part 2 monkey business: ", inspections[0]*inspections[1])


def my_function():
    with open('aoc11_data.txt', 'r') as f:
    #with open('aoc11_data_test.txt', 'r') as f:
        data = f.read().splitlines()

    data.append('')
    monkeys = []
    for line in data:
        if line.startswith('Monkey '):
            n = int(line.split(' ')[1].replace(':', ''))
        elif line.startswith('  Starting items: '):
            items = [int(el) for el in line.strip().replace(',','').split(' ') if el.isnumeric()]
        elif line.startswith('  Operation: new = old '):
            operation = line.replace('  Operation: new = old ', '')
        elif line.startswith('  Test: divisible by '):
            test = int(line.replace('  Test: divisible by ', ''))
        elif line.startswith('    If true: throw to monkey '):
            true_throw = int(line.replace('    If true: throw to monkey ', ''))
        elif line.startswith('    If false: throw to monkey '):
            false_throw = int(line.replace('    If false: throw to monkey ', ''))
        elif line == '':
            monkeys.append(Monkey(number=n, items=items, operation=operation, test=test, true_throw=true_throw, false_throw=false_throw))

    for r in range(1, 21):
        for m in monkeys:
            m.inspections += len(m.items)
            for item in m.items:
                if m.operation == '* old':
                    new_item = item*item
                elif m.operation.startswith('*'):
                    new_item = item * int(m.operation.replace('* ', ''))
                elif m.operation.startswith('+'):
                    new_item = item + int(m.operation.replace('+ ', ''))
                new_item = math.floor(new_item/3)
                if new_item % m.test == 0:
                    monkeys[m.true_throw].items.append(new_item)
                else:
                    monkeys[m.false_throw].items.append(new_item)
            m.items = []

    inspections = sorted([m.inspections for m in monkeys], reverse=True)
    print("answer part 1 monkey business: ", inspections[0]*inspections[1])


if __name__ == "__main__":
    start = time.time()
    my_function()
    my_function2()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


