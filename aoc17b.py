"""
Advent of code day 17 in python.
"""

import sys
import re
from math import sqrt

with open("aoc17.in" if len(sys.argv) < 2 else sys.argv[1], encoding="utf-8") as f:
    # data = [re.findall(r'[a-z]+', x) for x in re.findall(r'[a-z ]+\|[a-z ]+', f.read())]
    # data = re.findall(r"(\w+)-(\w+)", f.read())
    data = re.findall(r"(-?\d+)\.\.(-?\d+)", f.read())
    # data = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', f.read())
    # data = [tuple(int(y) for y in tup) for tup in data]

xrange = (int(data[0][0]), int(data[0][1]))
yrange = (int(data[1][0]), int(data[1][1]))


def dostep(xpos, ypos, xvol, yvol):
    xpos += xvol
    ypos += yvol
    if xvol > 0:
        xvol -= 1
    if xvol < 0:
        xvol += 1
    yvol -= 1
    return (xpos, ypos, xvol, yvol)


def fitsx(xvol):
    state = [0, 0, xvol, 0]
    height = 0
    while True:
        state = dostep(*state)
        if xrange[0] <= state[0] <= xrange[1]:
            return True
        if state[2] == 0 or state[0] > xrange[1]:
            return False


def fitsy(yvol):
    state = [0, 0, 0, yvol]
    while True:
        state = dostep(*state)
        if yrange[0] <= state[1] <= yrange[1]:
            return True
        if state[1] < yrange[0]:
            return False


def maxheight(xvol, yvol):
    state = [0, 0, xvol, yvol]
    height = 0
    while True:
        state = dostep(*state)
        height = max(height, state[1])
        if xrange[0] <= state[0] <= xrange[1] and yrange[0] <= state[1] <= yrange[1]:
            return height
        if state[0] > xrange[1] or state[1] < yrange[0]:
            return None


possible_x = [
    xvol for xvol in range(int(sqrt(xrange[0] * 2)) - 1, xrange[1] + 2) if fitsx(xvol)
]
possible_y = [yvol for yvol in range(yrange[0] - 1, -yrange[0] + 2) if fitsy(yvol)]

highest = 0
count = 0
athighest = (1, 1)
for xvol in possible_x:
    for yvol in possible_y:
        high = maxheight(xvol, yvol)
        if high is not None and high > highest:
            highest = high
            athighest = (xvol, yvol)
        if high is not None:
            count += 1
print(highest, athighest, count)
