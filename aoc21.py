#! /usr/bin/python

import time
import math

data = {}


def get_equation_from_monkey_key(mk):
    this_case = data[mk]
    if this_case.isnumeric():
        return int(this_case)
    if ' + ' in this_case:
        mk1, mk2 = this_case.split(' + ')
        return '({}+{})'.format(get_equation_from_monkey_key(mk1), get_equation_from_monkey_key(mk2))
    elif ' - ' in this_case:
        mk1, mk2 = this_case.split(' - ')
        return '({}-{})'.format(get_equation_from_monkey_key(mk1), get_equation_from_monkey_key(mk2))
    elif ' * ' in this_case:
        mk1, mk2 = this_case.split(' * ')
        return '({}*{})'.format(get_equation_from_monkey_key(mk1), get_equation_from_monkey_key(mk2))
    elif ' / ' in this_case:
        mk1, mk2 = this_case.split(' / ')
        return '({}/{})'.format(get_equation_from_monkey_key(mk1), get_equation_from_monkey_key(mk2))
    else:
        print(this_case)


def get_solutions(changes):
    ret_solutions = {}
    for eq in changes:
        if '+' in eq:
            mk1, mk2 = eq.replace('(', '').replace(')', '').split('+')
            ret_solutions[eq] = int(mk1) + int(mk2)
        elif '-' in eq:
            mk1, mk2 = eq.replace('(', '').replace(')', '').split('-')
            ret_solutions[eq] = int(mk1) - int(mk2)
        elif '*' in eq:
            mk1, mk2 = eq.replace('(', '').replace(')', '').split('*')
            ret_solutions[eq] = int(mk1) * int(mk2)
        elif '/' in eq:
            mk1, mk2 = eq.replace('(', '').replace(')', '').split('/')
            # print("is integer:", (int(mk1) / int(mk2)).is_integer())
            ret_solutions[eq] = round(int(mk1) / int(mk2))
        else:
            print("should never happen: ", eq)
    return ret_solutions


def my_function():
    with open('aoc21_data.txt', 'r') as f:
    #with open('aoc21_data_test.txt', 'r') as f: # 252 is too low
        data_r = f.readlines()
    global data
    data = {el.strip().split(':')[0].strip(): el.strip().split(':')[1].strip() for el in data_r}

    case = data['root']
    ans = '({} + {})'.format(get_equation_from_monkey_key(case.split(' + ')[0]), get_equation_from_monkey_key(case.split(' + ')[1]))

    i = 0
    while '(' in ans:
        changes = []
        for id_c, c in enumerate(ans):
            if c == '(':
                close_para = ans.index(')', id_c)
                if '(' in ans[id_c + 1:] and id_c+1 < len(ans):
                    open_para = ans.index('(', id_c+1)
                else:
                    open_para = len(ans)+ 100
                if close_para < open_para:
                    simple_eq = ans[id_c:close_para+1]
                    changes.append(simple_eq)
        solutions = get_solutions(changes)
        for k in solutions.keys():
            ans = ans.replace(k, str(solutions[k]))
        i += 1
        # print(i, ans)
    print("answer part 1:", ans)


def my_function2():
    with open('aoc21_data.txt', 'r') as f:
    #with open('aoc21_data_test.txt', 'r') as f: # 252 is too low
        data_r = f.readlines()
    #print(len(data_r))
    global data
    data = {el.strip().split(':')[0].strip(): el.strip().split(':')[1].strip() for el in data_r}

    case = data['root']
    for humn in range(int(3.558714869434*10**12), int(3.558714869439*10**12)):# range(290, 310):#, 0, 10000]:
        # print(" now trying", humn)
        data['humn'] = str(humn)#10000
        ans = '({} - {})'.format(get_equation_from_monkey_key(case.split(' + ')[0]),
                                 get_equation_from_monkey_key(case.split(' + ')[1]))
        i = 0
        while '(' in ans:
            changes = []
            for id_c, c in enumerate(ans):
                if c == '(':
                    close_para = ans.index(')', id_c)
                    if '(' in ans[id_c + 1:] and id_c+1 < len(ans):
                        open_para = ans.index('(', id_c+1)
                    else:
                        open_para = len(ans)+ 100
                    if close_para < open_para:
                        simple_eq = ans[id_c:close_para+1]
                        changes.append(simple_eq)
            solutions = get_solutions(changes)
            for k in solutions.keys():
                ans = ans.replace(k, str(solutions[k]))
            i += 1
        print(humn, ans)
    print("part 2 answer: 3558714869436 gives answer 0 and yields integer answer on all divisions")


if __name__ == "__main__":
    start = time.time()
    my_function()
    my_function2()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


