#!/usr/bin/env python3

def find_dupe(first, last):
    for x in first:
        for y in last:
            if x == y:
                return x

def get_point_vaule(item):
    o = ord(item)
    if o < 97:
        return ord(item) - 38
    else:
        return ord(item) - 96

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

total = 0
for items in lines:
    halfway = int(len(items)/2)
    first = items[:halfway]
    last = items[halfway:]

    dupe = find_dupe(first, last)

    points = get_point_vaule(dupe)

    print(first, last, dupe, points)
    total += points

print('total:', total)
