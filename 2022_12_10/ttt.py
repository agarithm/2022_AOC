#!/usr/bin/python3

import sys
import pprint
from dataclasses import dataclass
from sys import getrefcount
pp = pprint.pprint

if len(sys.argv) != 2:
    print("\n Usage: ttt.py input_file \n\n")

fname = sys.argv[1];
with open(fname) as f:
    instructions = f.read().splitlines()

####################################################################################
## Helpers


def paint(g):
    for x in range(len(g)-1,-1,-1):
        for y in range(0,len(g)):
            print(g[x][y],end="")
        print(" ")


def grid(x,y):
    out = []
    for i in range(0,x):
        row = []
        for j in range(0,y):
            row.append(".")
        out.append(row)
    return out

@dataclass
class Pos:
    x: int
    y: int


def printMap(move):
    global knots
    gridSize = 10
    for k in knots:
        gridSize = max(abs(k.x),abs(k.y),gridSize)

    map = grid(gridSize*2+1,gridSize*2+1)

    map[gridSize][gridSize] = "S"
    for i in range(knotCount-1,-1,-1):
        k=knots[i]
        x = gridSize + k.x
        y = gridSize + k.y
        map[y][x] = str(i) if i > 0 else "H"

    print("")
    print(f"== {move} ==")
    print("")
    paint(map)

def up(p):
    return Pos(p.x,p.y+1)

def down(p):
    return Pos(p.x,p.y-1)

def right(p):
    return Pos(p.x+1,p.y)

def left(p):
    return Pos(p.x-1,p.y)

shift = {
        'U': up,
        'D': down,
        'R': right,
        'L': left,
        }


####################################################################################
## SOLVER

x = 1
ticks = [x]

for i in instructions:
    parts = i.split(" ")
    cmd = parts[0]
    count = int(parts[1]) if len(parts) > 1 else 1
    if cmd == "noop":
        ticks.append(x)
    else:
        ticks.append(x)
        x += count
        ticks.append(x)

strength = 0
for i in range(20,len(ticks)-1,40):
    print(f"{i} ==> {ticks[i-1]}")
    strength += ticks[i-1]*(i)

print(f"strength = {strength}")

while len(ticks) >= 40:
    for x in range(0,40):
        pos = ticks.pop(0)
        if pos == x or pos+1 == x or pos-1 == x:
            print("#",end="")
        else:
            print(".",end="")

    print()


