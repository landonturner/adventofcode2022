#!/usr/bin/env python3

class Head:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tail = None
        self.tailHistory = []
    
    def move(self, direction, magnitude):
        print(f"moving {magnitude} spaces {direction}")
        for _ in range(magnitude):
            if direction == "R":
                self.x = self.x + 1
            elif direction == "L":
                self.x = self.x - 1
            elif direction == "U":
                self.y = self.y + 1
            else:
                self.y = self.y - 1
            self.tail.follow()
            print("from move", self, self.tail)
    
    def __str__(self):
        return f"{self.x}, {self.y}"

class Tail:
    def __init__(self, number, head):
        self.number = number
        self.x = 0
        self.y = 0
        self.head = head
        self.tail = None
        self.visited = set()
        
    def move_toward_head_x(self):
        if self.x == self.head.x:
            raise "THIS SHITS BAD"
        if self.x > self.head.x:
            self.x -= 1
        else:
            self.x += 1

    def move_toward_head_y(self):
        if self.y == self.head.y:
            raise "THIS SHITS BAD"
        if self.y > self.head.y:
            self.y -= 1
        else:
            self.y += 1


    def follow(self):
        # if not more than one space away, do nothing
        head_x = self.head.x
        head_y = self.head.y
        if abs(self.x - head_x) <= 1 and abs(self.y - head_y) <= 1:
            print("doing nothing", self, self.head)
        else:
            # check diagonal first
            if abs(self.x - head_x) >= 1 and abs(self.y - head_y) >= 1:
                self.move_toward_head_x()
                self.move_toward_head_y()
            elif self.x == head_x:
                self.move_toward_head_y()
            elif self.y == head_y:
                self.move_toward_head_x()
            else:
                raise "WACKY WEDNESDAY"
        self.visited.add((self.x, self.y))
        print(self.tail)
        if self.tail is not None:
            self.tail.follow()
    
    def __str__(self):
        return f"{self.number} - ({self.x}, {self.y})"

def run(lines):
    head = Head()
    tails = [Tail(0, head)]
    head.tail = tails[0]
    for i in range(8):
        tails.append(Tail(i + 1, tails[-1]))
        tails[i].tail = tails[i+1]


    for line in lines:
        direction, magnitude = line.split(" ")
        head.move(direction, int(magnitude))
        print(line)
    print(len(tails[-1].visited))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines)
