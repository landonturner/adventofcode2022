#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

encoding = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

win_chart = {
    'rock': 'scissors', # rock beats scissors
    'paper': 'rock', # paper beats rock
    'scissors': 'paper', # scissors beats paper
}

reverse_win_chart = {
    'scissors': 'rock', # rock beats scissors
    'rock': 'paper', # paper beats rock
    'paper': 'scissors', # scissors beats paper
}

point_chart = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

points = 0

for r in lines:
    them_raw, me_raw = r.split()
    them = encoding[them_raw]
    state = encoding[me_raw]
    me = them
    if state == 'win':
        me = reverse_win_chart[them]
    elif state == 'lose':
        me = win_chart[them]

    points += point_chart[me]
    if them == me:
        points += 3
    elif win_chart[me] == them:
        points += 6

print(points)


