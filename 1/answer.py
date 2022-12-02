#!/usr/bin/env python3

groups = []
with open('./input.txt', 'r') as f:
    current = 0
    for line in f.readlines():
        l = line.strip()
        print('line: ', l)
        if l == '':
            groups.append(current)
            current = 0
        else:
            current = current + int(l)
groups.sort()
print("largest group:", groups)

