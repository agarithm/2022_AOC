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
    moves = f.read().splitlines()

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


def ceil(n,d):
    q, r = divmod(n, d)
    return int(q + bool(r))


def dragTail(head, tail):
    dx = abs(head.x-tail.x)
    dy = abs(head.y-tail.y)
    return True if (dx>1 or dy>1) else False

def gapDirection(head,tail,direction):
    out = direction
    dx = head.x - tail.x
    dy = head.y - tail.y
    if abs(dx) > abs(dy) and abs(dx) != abs(dy):
        out = 'R' if head.x > tail.x else 'L'
    elif abs(dx) < abs(dy) and abs(dx) != abs(dy):
        out = 'U' if head.y > tail.y else 'D'

    return out


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

def join(head,tail):
    out = None

    def diff(d):
        if d == 0:
            return 0
        elif d < 0:
            return -1
        else:
            return 1
        #return ceil(d,2)

    dx = head.x - tail.x
    dy = head.y - tail.y

    out = Pos(tail.x+diff(dx), tail.y+diff(dy))
    def p(x):
        return f"[{x.x},{x.y}]"

    print(f" {p(head)} and {p(tail)} = {p(out)} ")
    return out


####################################################################################
## SOLVER

knotCount = 10
knots: [Pos] = []
tracks = []

for i in range(0,knotCount):
        knot = Pos(0,0)
        knots.append(knot)
        tracks.append([])
        tracks[i].append(knot)

for move in moves:
    parts = move.split(' ')
    direction = parts[0]
    steps = int(parts[1])
    for i in range(0,steps):
        print(f"{direction} {steps}:{i}")
        knots[0] = shift.get(direction)(knots[0])
        tracks[0].append(knots[0])
        for j in range(0,knotCount-1):
            head = knots[j];
            tail = knots[j+1];
            if dragTail(head,tail):
                knots[j+1] = join(head,tail)
                tracks[j+1].append(knots[j+1])
    #printMap(move)

tailVisits = {}
for p in tracks[knotCount-1]:
    key = str(p.x)+","+str(p.y)
    tailVisits[key]=p

pp(len(tailVisits))
