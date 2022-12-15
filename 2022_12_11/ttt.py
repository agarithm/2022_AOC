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
    notes = f.read().splitlines()

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

#dataclass
class Monkey:
    items = []
    operand = ""
    op = ""
    denom = 1
    true = 0
    false = 0
    inspections = 0

monkeys = []
while len(notes) >= 6:
    line = notes.pop(0)
    if len(line) == 0:
        continue
    monkey = Monkey()
    monkey.items = []
    line = notes.pop(0)
    pp(line)
    parts = line.split(":")
    parts = parts[1].split(",")
    for part in parts:
        if len(part):
            monkey.items.append(int(part.strip()))
    line = notes.pop(0)
    parts = line.split(" ")
    monkey.operand = parts[len(parts)-1].strip()
    monkey.op = parts[len(parts)-2]
    line = notes.pop(0)
    parts = line.split(" ")
    monkey.denom = int(parts[len(parts)-1])
    line = notes.pop(0)
    parts = line.split(" ")
    monkey.true = int(parts[len(parts)-1])
    line = notes.pop(0)
    parts = line.split(" ")
    monkey.false = int(parts[len(parts)-1])
    monkeys.append(monkey)


for monkey in monkeys:
    pp("###########################")
    pp(monkey.items)
    pp(monkey.operand)
    pp(monkey.op)
    pp(monkey.denom)
    pp(monkey.true)
    pp(monkey.false)


for round in range(0,20):
    for monkey in monkeys:
        for worry in monkey.items:
            monkey.inspections += 1
            operand = int(monkey.operand) if monkey.operand != 'old' else worry
            if monkey.op == '+':
                worry += operand
            elif monkey.op == '*':
                worry *= operand
            worry = int(worry/3)
            if worry % monkey.denom == 0:
                monkeys[monkey.true].items.append(worry)
            else:
                monkeys[monkey.false].items.append(worry)
        monkey.items = []

    pp("End Round " + str(round), width=200)
    for monkey in monkeys:
        pp(monkey.items)

monkey_business = []
for monkey in monkeys:
    monkey_business.append(monkey.inspections)

monkey_business = sorted(monkey_business,reverse=True)
pp(monkey_business)

print(f"Answer: {monkey_business[0]*monkey_business[1]}")

print("################## PART 2 #########################")

fname = sys.argv[1];
with open(fname) as f:
    notes = f.read().splitlines()

monkeys = []
while len(notes) >= 6:
    line = notes.pop(0)
    if len(line) == 0:
        continue
    monkey = Monkey()
    monkey.items = []
    line = notes.pop(0)
    pp(line)
    parts = line.split(":")
    parts = parts[1].split(",")
    for part in parts:
        if len(part):
            monkey.items.append(int(part.strip()))
    line = notes.pop(0)
    parts = line.split(" ")
    monkey.operand = parts[len(parts)-1].strip()
    monkey.op = parts[len(parts)-2]
    line = notes.pop(0)
    parts = line.split(" ")
    monkey.denom = int(parts[len(parts)-1])
    line = notes.pop(0)
    parts = line.split(" ")
    monkey.true = int(parts[len(parts)-1])
    line = notes.pop(0)
    parts = line.split(" ")
    monkey.false = int(parts[len(parts)-1])
    monkeys.append(monkey)

lcm = 1;
for monkey in monkeys:
    pp("###########################")
    pp(monkey.items)
    pp(monkey.operand)
    pp(monkey.op)
    pp(monkey.denom)
    pp(monkey.true)
    pp(monkey.false)
    lcm *= monkey.denom



for round in range(0,10000):
    for monkey in monkeys:
        for worry in monkey.items:
            monkey.inspections += 1
            operand = int(monkey.operand) if monkey.operand != 'old' else worry
            if monkey.op == '+':
                worry += operand
            elif monkey.op == '*':
                worry *= operand
            if worry % monkey.denom == 0:
                monkeys[monkey.true].items.append(worry%lcm)
            else:
                monkeys[monkey.false].items.append(worry%lcm)
        monkey.items = []

    if round % 100 == 0:
        pp("End Round " + str(round), width=200)
        monkey_business = []
        for monkey in monkeys:
            monkey_business.append(monkey.inspections)

        monkey_business = sorted(monkey_business,reverse=True)
        pp(monkey_business)

monkey_business = []
for monkey in monkeys:
    monkey_business.append(monkey.inspections)

monkey_business = sorted(monkey_business,reverse=True)
pp(monkey_business)

print(f"Answer: {monkey_business[0]*monkey_business[1]}")
