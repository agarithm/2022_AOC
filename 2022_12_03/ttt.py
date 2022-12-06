#!/usr/bin/python3

import sys
from dataclasses import dataclass

if len(sys.argv) != 2:
    print("\n Usage: ttt.py input_file \n\n")

fname = sys.argv[1];
with open(fname) as f:
        bags = f.read().splitlines()

@dataclass
class Compartment:
    contents: [str]

@dataclass
class Sack:
    contents: str
    left: Compartment = None
    right: Compartment = None
    common: str = None
    priority: int = 0

def calcPriority(c: str):
    if ord(c) > 90:
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


sacks: [Sack] = []
for bag in bags:
     sack = Sack( contents=bag )
     sack.left = Compartment(contents=list(sack.contents[:int(len(sack.contents)/2)]))
     sack.right = Compartment(contents=list(sack.contents[int(len(sack.contents)/2):]))
     for c in sack.left.contents:
         if c in sack.right.contents:
             sack.common = c
             sack.priority = calcPriority(c)
             break
     print(f"{sack}")
     sacks.append(sack)

total = 0;
for sack in sacks:
    total += sack.priority

print(f"Sum of priorities: {total}")

total = 0
while sacks:
    a = sacks.pop()
    b = sacks.pop()
    c = sacks.pop()
    aList = list(a.contents)
    bList = list(b.contents)
    cList = list(c.contents)
    for x in aList:
        if x in bList and x in cList:
            total += calcPriority(x)
            break

print(f"Sum of priorities: {total}")
