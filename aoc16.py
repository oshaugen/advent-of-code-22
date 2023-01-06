import time
from queue import Queue
from itertools import permutations

flow = {}
tunnels = {}
distance = {}


def parse(filename):
    with open(filename) as f:
        data = [ l.strip().split("; ")  for l in f.readlines() ]
        tunnels = {}
        flow = {}
        for d in data:
            v = d[0].split(" has flow rate=")
            V = v[0].replace("Valve ","")
            F = int(v[1])
            T = d[1].replace("tunnels lead to valves ","").replace("tunnel leads to valve ","").split(", ")
            flow[V] = F
            tunnels[V] = T
        return flow, tunnels


def trace_path(V1, V2):#,tunnels):
    '''Simple BFS search of shortest path between valve V1 and V2'''
    path = [V1]
    q = Queue()
    q.put(path)
    visited = [ V1 ]
    while not q.empty():
        path = q.get()
        for v in tunnels[ path[-1] ]:
            if v not in visited:
                if v==V2:
                    return path+[v]
                else:
                    pathnew = list(path)
                    pathnew.append(v)
                    q.put(pathnew)
    print("not found")
    return None


def calculate(rp, min=0):#, tunnels):
    #min = 0
    tot = 30
    score = 0
    i = 0
    valve_nodes = rp.split('#')
    while (i+1) < len(valve_nodes):
        steps = distance[(valve_nodes[i], valve_nodes[i+1])]
        min += steps
        if min >= tot:
            break
        min += 1
        score += (30-min)*flow[valve_nodes[i+1]]
        if min >= tot:
            break
        i += 1
    return score, min


def part1():
    global flow
    global tunnels
    flow, tunnels = parse('aocdata16.txt')
    #flow, tunnels = parse('aocdata16_test.txt')
    rel_paths = ['AA']

    have_flow = sorted([v for v, f in flow.items() if f > 0])


    have_flow.extend(rel_paths.copy())
    global distance
    for k1 in have_flow:
        for k2 in have_flow:
            if k1 != k2 and (k1, k2) not in distance.keys():
                distance[(k1, k2)] = len(trace_path(k1, k2))-1
                distance[(k2, k1)] = len(trace_path(k1, k2))-1

    new_paths = {'AA': 0}
    paths = {}
    i = 0
    best_flow = 0
    while i < 13:
        i += 1
        paths_to_expand = {el: new_paths[el] for el in new_paths.keys()}
        #print(i, len(paths), len(paths_to_expand))
        new_paths = {}
        for p in paths_to_expand.keys():
            was_expanded = False
            for poss_next in have_flow:
                if poss_next in p:
                    continue
                p_last = p.split('#')[-1]
                if paths_to_expand[p] + distance[(p_last, poss_next)] >= 30:
                    continue
                new_p = p + '#' + poss_next
                was_expanded = True
                new_paths[new_p] = paths_to_expand[p] + distance[(p_last, poss_next)]
            if not was_expanded:
                paths[p] = paths_to_expand[p]

    for p in paths.keys():
        p_flow, p_min = calculate(rp=p)
        if p_flow > best_flow:
            #print(p, paths[p])
            best_flow = p_flow
            #print("best_flow", best_flow)
    print("answer part 1", best_flow)
    return


def part2():
    global flow
    global tunnels
    flow, tunnels = parse('aocdata16.txt')
    #flow, tunnels = parse('aocdata16_test.txt')
    rel_paths = ['AA']

    have_flow = sorted([v for v, f in flow.items() if f > 0])

    have_flow.extend(rel_paths.copy())
    global distance
    for k1 in have_flow:
        for k2 in have_flow:
            if k1 != k2 and (k1, k2) not in distance.keys():
                distance[(k1, k2)] = len(trace_path(k1, k2))-1
                distance[(k2, k1)] = len(trace_path(k1, k2))-1

    new_paths = {'AA': 0}
    paths = {}
    i = 0
    best_flow = 0
    while i < 13:
        i += 1
        paths_to_expand = {el: new_paths[el] for el in new_paths.keys()}
        #print(i, len(paths), len(paths_to_expand))
        new_paths = {}
        for p in paths_to_expand.keys():
            for poss_next in have_flow:
                if poss_next in p:
                    continue
                p_last = p.split('#')[-1]
                if paths_to_expand[p] + distance[(p_last, poss_next)] >= 26:
                    continue
                new_p = p + '#' + poss_next
                new_paths[new_p] = paths_to_expand[p] + distance[(p_last, poss_next)]
            paths[p] = paths_to_expand[p]

    #print("# paths", len(paths))

    paths_with_keys = {}
    for p in paths.keys():
        p_sorted_set_key = ''.join(sorted(p.split('#')))
        if p_sorted_set_key in paths_with_keys.keys():
            paths_with_keys[p_sorted_set_key].append(p)
        else:
            paths_with_keys[p_sorted_set_key] = [p]

    paths_with_keys_best_path_score = {}
    for p in paths_with_keys.keys():
        if len(p) < 10: # minimum five elements
            continue
        best_path, best_score = '', 0
        for t_path in paths_with_keys[p]:
            score, min = calculate(t_path, 4)
            if score > best_score:
                best_path = t_path
                best_score = score
        paths_with_keys_best_path_score[best_path] = best_score

    best_answer = 0
    pbk_keys = list(paths_with_keys_best_path_score.keys())
    len_pbk_keys = len(pbk_keys)
    for i in range(0, len_pbk_keys-1):
        p1 = pbk_keys[i]
        p1_list = p1.split('#')
        for j in range(i+1, len_pbk_keys):
            p2 = pbk_keys[j]
            p2_list = p2.split('#')
            if len(set(p1_list + p2_list)) + 1 == len(set(p1_list)) + len(set(p2_list)):
                 temp_answer = paths_with_keys_best_path_score[p1] + paths_with_keys_best_path_score[p2]
                 if temp_answer > best_answer:
                     best_answer = temp_answer
                     #print("best so far:", p1, p2, best_answer)
    print("answer part 2", best_answer)
    return


if __name__ == '__main__':
    start = time.time()
    part1()
    part2()
    print('Finished in {} seconds'.format(round(time.time() - start, 1)))