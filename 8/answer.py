#!/usr/bin/env python3

def column(grid, i):
    return [int(row[i]) for row in grid]

def count_left(index, array):
    if index == 0:
        return 0
    count = 0
    for i in range(index - 1, -1, -1):
        count += 1
        if array[i] >= array[index]:
            return count
    return count

def count_right(index, array):
    if index + 1 == len(array):
        return 0
    count = 0
    for i in range(index + 1, len(array)):
        count += 1
        if array[i] >= array[index]:
            return count
    return count

def run(forest):
    visible_count = 0

    columns = [column(forest, i) for i in range(len(forest))]

    highest_score = 0

    for y in range(99):
        for x in range(99):
            row = forest[y]
            col = columns[x]

            left = count_left(x, row)
            right = count_right(x, row)
            up = count_left(y, col)
            down = count_right(y, col)

            score = left * right * up * down
            if score > highest_score:
                highest_score = score
    print('highest score', highest_score)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    forest = []
    for line in lines:
        forest.append([int(x) for x in line])
    run(forest)
    # line = forest[0]
    # for i in range(len(line)):
    #     print(i, line[i], count_left(i, line), count_right(i, line))


