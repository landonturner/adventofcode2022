#!/usr/bin/env python3

def find_dupe(first, second, third):
    for x in first:
        for y in second:
            if x == y:
                for z in third:
                    if z == x:
                        return z

def get_point_vaule(item):
    o = ord(item)
    if o < 97:
        return ord(item) - 38
    else:
        return ord(item) - 96

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

total = 0
group = []
for items in lines:
    group.append(items)
    if len(group) == 3:
        dupe = find_dupe(group[0], group[1], group[2])
        print('dupe:', dupe)
        points = get_point_vaule(dupe)
        total += points
        group = []

print('total:', total)
