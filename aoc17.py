import time
import math

# def get_top_rock(matrix):
#     rev_matrix = matrix.copy()
#     rev_matrix.reverse()
#     for idx, row in enumerate(rev_matrix):
#         if '#' not in row:
#             return idx


def get_top_rock2(stones):
    if not stones:
        return -1
    m = max([el[1] for el in stones])
    return m


def get_rock_positions(floor, c):
    c_mod = c % 5
    floor = floor + 1
    if c_mod == 0:  
        #      c###
        pos = [(2, floor+3), (3, floor+3), (4, floor+3), (5, floor+3)]
    elif c_mod == 1:
        #       #
        #      c##
        #       #
        pos = [(2, floor+4), (3, floor+4), (4, floor+4), (3, floor+5), (3, floor+3)]
    elif c_mod == 2:
        #        #
        #        #
        #      c##
        pos = [(2, floor+3), (3, floor+3), (4, floor+3), (4, floor+4), (4, floor+5)]
    elif c_mod == 3:
        #        #
        #        #
        #        #
        #        c
        pos = [(2, floor+3), (2, floor+4), (2, floor+5), (2, floor+6)]
    elif c_mod == 4:
        #       ##
        #       c#
        pos = [(2, floor+3), (3, floor+3), (2, floor+4), (3, floor+4)]
    return pos


def do_jet(positions, jet, stones):
    new_pos = []
    if jet == '>':
        delta = 1
    elif jet == '<':
        delta = -1
    else:
        print(jet)
        exit()
    for pos in positions:
        new_pos.append((pos[0]+delta, pos[1]))
    most_left = min([p[0] for p in new_pos])
    most_right = max([p[0] for p in new_pos])
    for p in new_pos:
        if p in stones:
            return positions
    if most_left >= 0 and most_right < 7:
        return new_pos
    return positions


def update_stones(stones, new_pos):
    new_stones = stones.copy()
    for p in new_pos:
        new_stones.append(p)
    return new_stones


def update_stones2(stones, new_pos):
    if stones:
        height_treshold = max([p[1] for p in stones])-100
        new_stones = [el for el in stones if el[1] > height_treshold]
    else:
        new_stones = stones.copy()

    for p in new_pos:
        new_stones.append(p)
    return new_stones


def draw(stones, counter):
    max_height = max([el[1] for el in stones]) + 5

    for i in range(0, max_height):
        row = max_height - 1 - i
        layer = ['.' for _ in range(7)]
        stones_in_layer = [el[0] for el in stones if el[1] == row]
        for s in stones_in_layer:
            layer[s] = '#'
        print(layer)


def main1():
    with open('aocdata17.txt', 'r') as f:
        jets_str = f.readline().strip()
        jets = []
        for _ in range(1):
            jets.extend([el for el in jets_str])
    #print(len(jets))
    #exit()
    stones = []

    counter = 0
    limit = 2022
    jet_iterator = 0
    while counter < limit:
        #if counter % 100 == 0:
        #    print(counter)

        # get new stone
        top_rock = get_top_rock2(stones)
        new_pos = get_rock_positions(top_rock, counter)
        steady = False
        while True:
            jet = jets[jet_iterator]
            jet_iterator += 1
            if jet_iterator == len(jets):
                jet_iterator = 0
            #jets.pop(0)
            # do jet
            new_pos = do_jet(new_pos, jet, stones)
            # do fall, if possible
            fall_pos = [(el[0], el[1]-1) for el in new_pos]
            for fp in fall_pos:
                if fp in stones or min([p[1] for p in fall_pos]) < 0:
                    steady = True
                    break
            if steady:
                stones = update_stones(stones=stones, new_pos=new_pos)
                break
            new_pos = fall_pos.copy()
        #draw(stones, counter)
        counter += 1
    print("answer part 1, height: ", max([p[1] for p in stones]) + 1)
    return


def draw_pattern(stones):
    height = max([p[1] for p in stones]) - 10
    relevant_stones = [(p[0], p[1] - height) for p in stones if (p[1] - height) > 0]
    row = ['.' for _ in range(7)]
    matrix = [row[::] for _ in range(11)]
    #print(matrix)
    for rs in relevant_stones:
        matrix[rs[1]][rs[0]] = '#'

    #for i in range(0, len(matrix)):
    #    col = len(matrix)-1 -i
    #    print(matrix[col])
    pattern = ''.join([''.join(row) for row in matrix])
    #print(pattern)
    return pattern


def main2():

    with open('aocdata17.txt', 'r') as f:
        jets_str = f.readline().strip()
        jets = []
        for _ in range(1):
            jets.extend([el for el in jets_str])
    #print(len(jets))

    counter_at_interest = 1000000000000
    #counter_at_interest = 100000 # answer: 150101

    cyclic_counter = math.floor((counter_at_interest-3120)/1715)
    rest_counter = counter_at_interest-3120 - (cyclic_counter*1715)

    stones = []
    counter = 0
    limit = 2022
    jet_iterator = 0
    reset = 0
    heights = []
    count_stones = []
    height = {}
    all_patterns = []
    pattern_found = False
    do_rest_counting = False
    rc = 0
    while counter < limit * 200:
        #if jet_iterator == 0:
        #    print(counter, jet_iterator, len(jets))

        # get new stone
        top_rock = get_top_rock2(stones)
        new_pos = get_rock_positions(top_rock, counter)
        steady = False
        while True:
            jet = jets[jet_iterator]
            jet_iterator += 1
            if jet_iterator == len(jets):
                jet_iterator = 0
                reset += 1
                if stones:
                    heightt = max([p[1] for p in stones]) + 1
                else:
                    heightt = 0
                heights.append(heightt)
                count_stones.append(counter)

                # rest_counter = 0
                # curr_height = max([p[1] for p in stones]) + 1

            new_pos = do_jet(new_pos, jet, stones)
            # do fall, if possible
            fall_pos = [(el[0], el[1]-1) for el in new_pos]
            for fp in fall_pos:
                if fp in stones or min([p[1] for p in fall_pos]) < 0:
                    steady = True
                    break
            if steady:
                stones = update_stones2(stones=stones, new_pos=new_pos)
                break
            new_pos = fall_pos.copy()

        #draw(stones, counter)
        counter += 1
        if do_rest_counting:
            rc += 1
        if counter == 3120:
            do_rest_counting = True
            rest_ref = max([p[1] for p in stones]) + 1
        if rc == rest_counter:
            rest_h = max([p[1] for p in stones]) + 1
            #print("restcounter", rest_counter, 'height:', rest_h, 'height diff:', rest_h-rest_ref)
            h_ans = 4711 + cyclic_counter * 2574 + (rest_h-rest_ref)
            print("answer part 2 for height {} is {}".format(counter_at_interest, h_ans))
            return

        if counter % 1000 == 0 or counter == 2022:
            height[counter] = max([p[1] for p in stones]) + 1
            #print(counter, height[counter] )
        new_pattern = '{}_{}'.format(counter % 5, draw_pattern(stones))
        if not pattern_found:
            if new_pattern in all_patterns:
                reference_pattern = new_pattern
                last_found = counter
                last_h = 0
                last_counter = 0
                pattern_found = True
                #print(counter, new_pattern)
        else:
            if new_pattern == reference_pattern:
                h = max([p[1] for p in stones]) + 1
                #print(counter, counter-last_found, new_pattern, h)
                if counter-last_found == 1245:
                    #print('height:', h, 'height diff:', h-last_h, 'counter:', counter, 'counter diff:', counter-last_counter)
                    last_h = h
                    last_counter = counter
                last_found = counter
        all_patterns.append(new_pattern)


if __name__ == '__main__':
    start = time.time()
    main1()
    main2()
    print('Finished in {} seconds'.format(round(time.time() - start, 1)))
