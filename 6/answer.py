#!/usr/bin/env python3

def all_different(marker):
    s = set(marker)
    if len(s) != len(marker):
        return False
    return True

def run(line):
    print(line)
    for i in range(len(line) - 4):
        packet_marker = line[i:i+4]
        if all_different(packet_marker):
            print('found a packet_marker', i+4)
            break

    for i in range(len(line) - 14):
        packet_marker = line[i:i+14]
        if all_different(packet_marker):
            print('found a message_marker', i+14)
            break


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines[0])
