import time


def main1():
    #with open('aocdata20_test.txt', 'r') as f:
    with open('aocdata20.txt', 'r') as f:
        digits = [int(el.strip()) for el in f.readlines()]

    n_digits = len(digits)
    unmoved_idx = [i for i in range(0, n_digits)]
    while True:
        idx = unmoved_idx.index(min([el for el in unmoved_idx if el >= 0]))
        mf = idx
        steps = digits[idx]
        mt = (idx + steps)# % n_digits
        while mt <= 0:
            mt += n_digits - 1
        while mt > n_digits-1:
            mt -= n_digits - 1
        new_digits, new_unmoved = [], []
        if mf < mt:
            temp_digits = [digits[0:mf], digits[mf+1:mt+1], [digits[mf]], digits[mt+1:]]
            temp_unmoved = [unmoved_idx[0:mf], unmoved_idx[mf+1:mt+1], [-1], unmoved_idx[mt+1:]]
        elif mf > mt:
            temp_digits = [digits[0:mt], digits[mf], digits[mt:mf], digits[mf+1:]]
            temp_unmoved = [unmoved_idx[0:mt], [-1], unmoved_idx[mt:mf], unmoved_idx[mf+1:]]
        elif mf == mt:
            temp_digits = digits.copy()
            temp_unmoved = [unmoved_idx[0:mt], [-1], unmoved_idx[mt+1:]]
        for td in temp_digits:
            if not isinstance(td, list):
                td = [td]
            new_digits.extend(td)
        for tu in temp_unmoved:
            if not isinstance(tu, list):
                tu = [tu]
            new_unmoved.extend(tu)
        digits = new_digits.copy()
        unmoved_idx = new_unmoved.copy()
        if max(unmoved_idx) < 0:
            break

    zero_idx = digits.index(0)
    index_of_interest = [(zero_idx+1000)%n_digits, (zero_idx+2000)%n_digits, (zero_idx+3000)%n_digits]
    sum = 0
    for idx in index_of_interest:
        # print(digits[idx])
        sum += digits[idx]
    print("part 1 answer:", sum)
    return


def do_mix(digits, unmoved_idx, n_digits):
    zero_done = False
    while True:
        if zero_done:
            minimum = min([el for el in unmoved_idx if el > 0])
            idx = unmoved_idx.index(minimum)
        else:
            minimum = min([el for el in unmoved_idx if el >= 0])
            idx = unmoved_idx.index(minimum)
            zero_done = True

        mf = idx
        steps = digits[idx]

        mt = (idx + steps)
        if mt < 0 or mt >= n_digits:
            mt = mt % (n_digits - 1)
        if mt == 0 and steps != 0:
            mt = n_digits - 1

        new_digits, new_unmoved = [], []
        if mf < mt:
            temp_digits = [digits[0:mf], digits[mf+1:mt+1], [digits[mf]], digits[mt+1:]]
            temp_unmoved = [unmoved_idx[0:mf], unmoved_idx[mf+1:mt+1], [-1*unmoved_idx[mf]], unmoved_idx[mt+1:]]
        elif mf > mt:
            temp_digits = [digits[0:mt], digits[mf], digits[mt:mf], digits[mf+1:]]
            temp_unmoved = [unmoved_idx[0:mt], [-1*unmoved_idx[mf]], unmoved_idx[mt:mf], unmoved_idx[mf+1:]]
        elif mf == mt:
            #print(now_moving)
            #exit()
            temp_digits = digits.copy()
            temp_unmoved = [unmoved_idx[0:mt], [-1*unmoved_idx[mf]], unmoved_idx[mt+1:]]
        for td in temp_digits:
            if not isinstance(td, list):
                td = [td]
            new_digits.extend(td)
        for tu in temp_unmoved:
            if not isinstance(tu, list):
                tu = [tu]
            new_unmoved.extend(tu.copy())
        digits = new_digits.copy()
        unmoved_idx = new_unmoved.copy()
        if max(unmoved_idx) <= 0:
            break
    return digits, unmoved_idx


def main2():
    decryption_key = 811589153
    #with open('aocdata20_test.txt', 'r') as f:
    with open('aocdata20.txt', 'r') as f:
        digits = [int(el.strip())*decryption_key for el in f.readlines()]
    n_digits = len(digits)
    unmoved_idx = [i for i in range(0, n_digits)]

    original_digits = digits.copy()
    updated_digits = digits.copy()
    for i in range(0, 10):
        ret_digits, unmoved_idx = do_mix(updated_digits, unmoved_idx, n_digits)
        unmoved_idx = [-1*el for el in unmoved_idx]
        updated_digits = [el for el in ret_digits]

    zero_idx = updated_digits.index(0)
    index_of_interest = [(zero_idx+1000)%n_digits, (zero_idx+2000)%n_digits, (zero_idx+3000)%n_digits]
    ans_sum = 0
    for idx in index_of_interest:
        # print(updated_digits[idx])
        ans_sum += updated_digits[idx]
    print("part 1 answer:", ans_sum)
    return


if __name__ == '__main__':
    start = time.time()
    main1()
    main2()

    print('Finished in {} seconds'.format(round(time.time() - start, 1)))
