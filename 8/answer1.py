#!/usr/bin/env python3

def column(grid, i):
    return [int(row[i]) for row in grid]

def check_left(index, array):
    if index == 0:
        return True
    for i in range(index):
        if array[i] >= array[index]:
            return False
    return True

def check_right(index, array):
    if index + 1 == len(array):
        return True
    for i in range(index + 1, len(array)):
        if array[i] >= array[index]:
            return False
    return True

def is_visible(index, array):
    """check_array determines if is visible in array given"""
    # check the smaller side first
    if index < len(array) / 2:
        visible = check_left(index, array)
        if visible:
            return True
        else:
            return check_right(index, array)
    else:
        visible = check_right(index, array)
        if visible:
            return True
        else:
            return check_left(index, array)


def run(forest):
    visible_count = 0

    columns = [column(forest, i) for i in range(len(forest))]

    for y in range(99):
        for x in range(99):
            row = forest[y]
            col = columns[x]
            print(x,y)
            # look left/right
            if is_visible(x, row):
                visible_count += 1
            else:
                # look up/down
                if is_visible(y, col):
                    visible_count += 1
    print('visible tree count', visible_count)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    forest = []
    for line in lines:
        forest.append([int(x) for x in line])
    run(forest)


