#!/usr/bin/env python3

import functools
import math


class Monkey:
    def __init__(self, number, items, op, divisible, true, false):
        self.inspections = 0
        self.number = number
        self.items = items
        self.op = op
        self.divisible = divisible
        self.true = true
        self.false = false

    def operate(self, item):
        self.inspections += 1
        lhs = 0
        rhs = 0
        if self.op[0] == "old":
            lhs = item
        else:
            lhs = int(self.op[0])

        if self.op[2] == "old":
            rhs = item
        else:
            rhs = int(self.op[2])
        
        if self.op[1] == "*":
            return lhs * rhs
        else:
            return lhs + rhs
    
    def test(self, item):
        if item % self.divisible == 0:
            return self.true
        return self.false

    def __str__(self):
        return f"Monkey {self.number} ({self.inspections}): {', '.join(map(str, self.items))}"
    
def run(lines):
    monkeys = []
    items = []
    op = []
    currentMonkey = 0
    divisible = 0
    true = 0
    false = 0
    for line in lines:
        if line == "":
            monkeys.append(Monkey(currentMonkey, items, op, divisible, true, false))
            currentMonkey += 1
            items = []
            op = []
            divisible = 0
            continue

        if line.startswith("Starting items:"):
            items = [int(x) for x in line.replace("Starting items: ", "").replace(",", "").split(" ")]

        if line.startswith("Operation: new = "):
            op = line.replace("Operation: new = ", "").split(" ")
        
        if line.startswith("Test: divisible by "):
            divisible = int(line.replace("Test: divisible by ", ""))

        if line.startswith("If true: throw to monkey "):
            true = int(line.replace("If true: throw to monkey ", ""))

        if line.startswith("If false: throw to monkey "):
            false = int(line.replace("If false: throw to monkey ", ""))

    monkeys.append(Monkey(currentMonkey, items, op, divisible, true, false))
    
    print("START")
    for m in monkeys:
        print(m)
    
    common_divisor = functools.reduce(lambda cd, x: cd * x, (m.divisible for m in monkeys))

    for i in range(10_000):
        print(f"ROUND {i + 1}")
        for m in monkeys:
            while len(m.items) > 0:
                # do the thing
                item = m.items.pop(0)
                new_level = m.operate(item) % common_divisor
                next_monkey = m.test(new_level)
                monkeys[next_monkey].items.append(new_level)

    monkeys.sort(key=lambda x: -x.inspections)
    for m in monkeys:
        print(m)
    
    print(f"{monkeys[0].inspections} x {monkeys[1].inspections} = {monkeys[0].inspections * monkeys[1].inspections}")
    

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines)
