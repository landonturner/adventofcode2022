#!/usr/bin/env python3

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.size} {self.name}\n"

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.directories = []
        self.files = []

    def size(self):
        total = 0
        for f in self.files:
            total += f.size
        for d in self.directories:
            total += d.size()
        return total

    def navigate(self, name):
        for c in self.directories:
            if c.name == name:
                return c
        return None

    def flatten(self):
        out = []
        out.extend(self.directories)
        for d in self.directories:
            out.extend(d.flatten())
        return out

    def __str__(self):
        return f"dir {self.name} - {self.size()}"

def parse(lines):
    root = Directory("root", None)
    cwd = root
    for line in lines:
        if line.startswith("$"):
            if line.startswith("$ cd"):
                # we are changing directories
                arg = line.split(" ")[2]
                if arg == "/":
                    cwd = root
                elif arg == "..":
                    cwd = cwd.parent
                else:
                    cwd = cwd.navigate(arg)
        else:
            # we have command output
            meta, name = line.split(" ")
            if meta == "dir":
                # add new directory to tree
                d = Directory(name, cwd)
                cwd.directories.append(d)
            else:
                # add file to current directory
                file = File(name, int(meta))
                cwd.files.append(file)
    return root

def run(lines):
    total_disk_space = 70000000
    target_disk_space = total_disk_space - 30000000

    root = parse(lines)

    current_disk_space = root.size()
    needed_to_reclaim = current_disk_space - target_disk_space

    closest_dir = root

    total = 0
    for d in root.flatten():
        size = d.size()
        if size >= needed_to_reclaim:
            if size < closest_dir.size():
                closest_dir = d
    print(closest_dir)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    run(lines)
