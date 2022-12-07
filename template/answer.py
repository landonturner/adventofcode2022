#!/usr/bin/env python3

def run(lines):
    for line in lines:
        print(line)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines)
