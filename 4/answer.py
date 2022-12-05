#!/usr/bin/env python3

def fully_contains(pair1, pair2):
    if pair1[0] < pair2[0]:
        return pair1[1] >= pair2[1]
    elif pair1[0] > pair2[0]:
        return pair2[1] >= pair1[1]
    else:
        # if they start at same time, one must contain other
        return True

def overlaps_at_all(pair1, pair2):
    if pair1[0] < pair2[0]:
        # check if start of pair 2 is in bounds of pair 1
        return pair2[0] <= pair1[1]
    elif pair1[0] > pair2[0]:
        # check if start of pair 1 is in bounds of pair 2
        return pair1[0] <= pair2[1]
    else:
        # if they start at same time, one must contain other
        return True

def parse_pair(pair):
    return [int(x) for x in pair.split('-')]

def run(lines):
    count = 0
    for assignments in lines:
        pair1, pair2 = [parse_pair(x) for x in assignments.split(',')]
        print('pairs:', pair1, pair2)
        if overlaps_at_all(pair1, pair2):
            count += 1
    print('pairs fully containing other pairs:', count)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines)
