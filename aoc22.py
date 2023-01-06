#! /usr/bin/python

import time
import math

maze_rows = []
maze_cols = []
cmds = []
face = 0


def get_next_cmd(ind):
    if cmds[ind] in ['R', 'L']:
        this_cmd = cmds[ind]
        ind += 1
    else:
        this_cmd = cmds[ind]
        while (ind+1) < len(cmds) and cmds[ind+1].isnumeric():
            this_cmd += cmds[ind+1]
            ind += 1
        ind += 1
    return this_cmd, ind


def get_new_col_pos(position, face, cmd):
    row = maze_rows[position[0]]
    eol = len(row)
    col_pos = position[1]
    steps = 0
    if face == 0:
        step = 1
        while steps < cmd:
            if col_pos + step == eol or row[col_pos + step] == ' ':
                if row.index('.') < row.index('#'):
                    col_pos = row.index('.')
                else:
                    break
            elif row[col_pos + step] == '#':
                break
            elif row[col_pos + step] == '.':
                col_pos = col_pos + step
            steps += 1
    elif face == 2:
        step = -1
        while steps < cmd:
            if col_pos + step < 0 or row[col_pos + step] == ' ':
                if row.rfind('.') > row.rfind('#'):
                    col_pos = row.rfind('.')
                else:
                    break
            elif row[col_pos + step] == '#':
                break
            elif row[col_pos + step] == '.':
                col_pos = col_pos + step
            steps += 1
    return position[0], col_pos


def get_new_row_pos(position, face, cmd):
    #print(cmd, type(cmd))
    col = maze_cols[position[1]]
    eol = len(col)
    row_pos = position[0]
    steps = 0
    if face == 1:
        step = 1
        while steps < cmd:
            if row_pos + step == eol or col[row_pos + step] == ' ':
                if col.index('.') < col.index('#'):
                    row_pos = col.index('.')
                else:
                    #col_pos = col_pos
                    break#return row_pos
            elif col[row_pos + step] == '#':
                break#return row_pos
            elif col[row_pos + step] == '.':
                row_pos = row_pos + step
            steps += 1
    elif face == 3:
        step = -1
        while steps < cmd:
            #print(row_pos + step)
            if row_pos + step < 0 or col[row_pos + step] == ' ':
                if col.rfind('.') > col.rfind('#'):
                    row_pos = col.rfind('.')
                else:
                    break
            elif col[row_pos + step] == '#':
                break
            elif col[row_pos + step] == '.':
                row_pos = row_pos + step
            steps += 1
    return row_pos, position[1]


def my_function():
    # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
    #with open('aoc22_data_test.txt', 'r') as f:

    global cmds
    global maze_rows
    global maze_cols

    with open('aoc22_data.txt', 'r') as f: # 113032
        data = f.readlines()
    print(data)
    cmds = data.pop()
    data.pop()
    maze_rows = [row.replace('\n', '') for row in data]
    max_row_length = max([len(r) for r in maze_rows])
    maze_rows = [r.ljust(max_row_length, ' ') for r in maze_rows]

    col = [el for el in range(0, len(maze_rows))]
    maze_cols = [col.copy() for _ in range(max_row_length)]
    for row_idx in range(0, len(maze_rows)):
        for col_idx in range(0, max_row_length):
            maze_cols[col_idx][row_idx] = maze_rows[row_idx][col_idx]
    maze_cols = [''.join(el) for el in maze_cols]

    position = (0, maze_rows[0].index('.'))
    face = 0
    ind = 0
    while ind < len(cmds):
        this_cmd, ind = get_next_cmd(ind)
        if this_cmd == 'R':
            face = (face+1) % 4
        elif this_cmd == 'L':
            face = (face-1) % 4
        else:
            if face in [0, 2]:
                position = get_new_col_pos(position, face, int(this_cmd))
            elif face in [1, 3]:
                position = get_new_row_pos(position, face, int(this_cmd))

    ans = 1000*(position[0]+1) + 4*(position[1]+1) + face
    print("answer part 1", ans)


def get_new_col_pos2(position, cmd):
    global face
    row = maze_rows[position[0]]
    eol = len(row)
    col_pos = position[1]
    steps = 0
    if face == 0:
        step = 1
        while steps < cmd:
            if col_pos + step == eol or row[col_pos + step] == ' ':
                if position[0] < 50:
                    p = (149 - position[0], 99)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 2
                    return get_new_col_pos2(p, cmd - steps - 1)
                elif position[0] < 100:
                    p = (49, position[0]+50)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 3
                    return get_new_row_pos2(p, cmd - steps - 1)
                elif position[0] < 150:
                    p = (149 - position[0], 149)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 2
                    return get_new_col_pos2(p, cmd - steps - 1)
                elif position[0] < 200:
                    p = (149, position[0]-100)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    # if p not #
                    face = 3
                    return get_new_row_pos2(p, cmd - steps - 1)
            elif row[col_pos + step] == '#':
                break
            elif row[col_pos + step] == '.':
                col_pos = col_pos + step
            steps += 1
    elif face == 2:
        step = -1
        while steps < cmd:
            if col_pos + step < 0 or row[col_pos + step] == ' ':
                if position[0] < 50:
                    p = (149 - position[0], 0)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 0
                    return get_new_col_pos2(p, cmd - steps - 1)
                elif position[0] < 100:
                    p = (100, position[0]-50)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 1
                    return get_new_row_pos2(p, cmd - steps - 1)
                elif position[0] < 150:
                    p = (149 - position[0], 50)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 0
                    return get_new_col_pos2(p, cmd - steps - 1)
                elif position[0] < 200:
                    p = (0, position[0]-100)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 1
                    return get_new_row_pos2(p, cmd - steps - 1)
            elif row[col_pos + step] == '#':
                break
            elif row[col_pos + step] == '.':
                col_pos = col_pos + step
            steps += 1
    return position[0], col_pos


def get_new_row_pos2(position, cmd):
    global face
    col = maze_cols[position[1]]
    eol = len(col)
    row_pos = position[0]
    steps = 0
    if face == 1:
        step = 1
        while steps < cmd:
            if row_pos + step == eol or col[row_pos + step] == ' ':
                if position[1] < 50:
                    p = (0, position[1] + 100)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 1
                    return get_new_row_pos2(p, cmd - steps - 1)
                elif position[1] < 100:
                    p = (position[1] + 100, 49)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 2
                    return get_new_col_pos2(p, cmd - steps - 1)
                elif position[1] < 150:
                    p = (position[1] - 50, 99)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 2
                    return get_new_col_pos2(p, cmd - steps - 1)
            elif col[row_pos + step] == '#':
                break
            elif col[row_pos + step] == '.':
                row_pos = row_pos + step
            steps += 1
    elif face == 3:
        step = -1
        while steps < cmd:
            if row_pos + step < 0 or col[row_pos + step] == ' ':
                if position[1] < 50:
                    p = (position[1] + 50, 50)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 0
                    return get_new_col_pos2(p, cmd - steps - 1)
                elif position[1] < 100:
                    p = (position[1] + 100, 0)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 0
                    return get_new_col_pos2(p, cmd - steps - 1)
                elif position[1] < 150:
                    p = (199, position[1] - 100)
                    if maze_rows[p[0]][p[1]] == '#':
                        break
                    face = 3
                    return get_new_row_pos2(p, cmd - steps - 1)

            elif col[row_pos + step] == '#':
                break
            elif col[row_pos + step] == '.':
                row_pos = row_pos + step
            steps += 1
    return row_pos, position[1]


def my_function2():
    # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
    #with open('aoc22_data_test.txt', 'r') as f:
    global cmds
    global maze_rows
    global maze_cols
    global face

    with open('aoc22_data.txt', 'r') as f: # 166188 too low
        data = f.readlines()
    cmds = data.pop()
    data.pop()
    maze_rows = [row.replace('\n', '') for row in data]
    max_row_length = max([len(r) for r in maze_rows])
    maze_rows = [r.ljust(max_row_length, ' ') for r in maze_rows]

    col = [el for el in range(0, len(maze_rows))]
    maze_cols = [col.copy() for _ in range(max_row_length)]
    for row_idx in range(0, len(maze_rows)):
        for col_idx in range(0, max_row_length):
            maze_cols[col_idx][row_idx] = maze_rows[row_idx][col_idx]
    maze_cols = [''.join(el) for el in maze_cols]

    position = (0, maze_rows[0].index('.'))
    ind = 0
    while ind < len(cmds):
        this_cmd, ind = get_next_cmd(ind)
        if this_cmd == 'R':
            face = (face+1) % 4
        elif this_cmd == 'L':
            face = (face-1) % 4
        else:
            if face in [0, 2]:
                position = get_new_col_pos2(position, int(this_cmd))
            elif face in [1, 3]:
                position = get_new_row_pos2(position, int(this_cmd))
    ans = 1000*(position[0]+1) + 4*(position[1]+1) + face
    print("answer part 2", ans)


if __name__ == "__main__":
    start = time.time()
    my_function()
    my_function2()
    end = time.time()
    print('Elapsed time: {} seconds'.format(end - start))


