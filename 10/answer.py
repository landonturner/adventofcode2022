#!/usr/bin/env python3

def run(lines):
    history = {}
    cycles = 1
    x = 1
    history[1] = 1

    for line in lines:
        print(line)
        op = line.split(' ')
        if len(op) > 1:
            if op[0] == "addx":
                print(f"incrementing x by {op[1]}")
                cycles += 1
                history[cycles] = x
                cycles += 1
                x += int(op[1])
                history[cycles] = x
        elif line == "noop":
            cycles += 1
            history[cycles] = x
            print("doing nothing")
        else:
            raise KeyError(f"got unexpected op: {op}")
        print(cycles, history[cycles])
    history[cycles] = x

    line = ""
    for i in range(300):
        if i != 0 and i % 40 == 0:
            print(line)
            line = ""
        current = i % 40
        val = history[i + 1]
        if abs(current - val) <= 1:
            line += "#"
        else:
            line += " "

    points = [20, 60, 100, 140, 180, 220]
    total = 0
    for p in points:
        total += history[p] * p
    
    print("total", total)
            
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines)
