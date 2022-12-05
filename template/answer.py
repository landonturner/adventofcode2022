#!/usr/bin/env python3

def run(lines):
    print(lines)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines)
