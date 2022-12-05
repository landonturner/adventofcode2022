#!/usr/bin/env python3

class Stack:
    def __init__(self, index):
        self.index = index
        self.items = []

    def init_add(self, item):
        self.items.insert(0, item)

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return f"{self.index}: {str(self.items)}"
    
class Stacks:
    stacks = []
    def __init__(self, length):
        for i in range(length):
            self.stacks.append(Stack(i))

    def init_stack_item(self, stack_index, item):
        self.stacks[stack_index].init_add(item)

    def move(self, number, from_stack, to_stack):
        for _ in range(number):
            self.stacks[to_stack].add(self.stacks[from_stack].pop())

    def __str__(self):
        result = ""
        for i, s in enumerate(self.stacks):
            result += f"{str(s)}\n"
        return result

def run(lines):
    stacks = Stacks(9)
    for line in lines:
        #print(line)
        if line == "":
            break

    parsing = True
    for line in lines:
        if parsing:
            if line[0] == '1':
                parsing = False
                continue
            z = line.replace('    ', " [_]").replace("[","").replace("]","").split(' ')
            for i, item in enumerate(z):
                if item == "_":
                    continue
                stacks.init_stack_item(i, item)
        else:
            # movements begin now
            if line == "":
                continue
            insts = line.split(' ')
            stacks.move(int(insts[1]), int(insts[3]) - 1, int(insts[5]) - 1)

    print(stacks)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines)
