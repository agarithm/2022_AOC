#!/usr/bin/python3

import sys
from dataclasses import dataclass

if len(sys.argv) != 2:
    print("\n Usage: ttt.py input_file \n\n")

fname = sys.argv[1];
with open(fname) as f:
        assignments = f.read().splitlines()


@dataclass
class Section:
    contents: str
    start: int = 0
    end: int = 0


@dataclass
class Assignment:
    contents: str
    left: Section = None
    right: Section = None


parsed: [Assignment] = []
for a in assignments:
     ass = Assignment( contents=a )
     sects = ass.contents.split(',')
     ass.left = Section(contents=sects[0],start=int(sects[0].split('-')[0]),end=int(sects[0].split('-')[1]))
     ass.right = Section(contents=sects[1],start=int(sects[1].split('-')[0]),end=int(sects[1].split('-')[1]))
     print(f"{ass}")
     parsed.append(ass)

overlap: [Assignment] = []
for a in parsed:
    if a.left.start <= a.right.start and a.left.end >= a.right.end:
        # Right in Left
        overlap.append(a)
    elif a.left.start >= a.right.start and a.left.end <= a.right.end:
        # Left in Right
        overlap.append(a)

for o in overlap:
    print(f"{o}")

print(f"Overlapping: {len(overlap)}")

overlap: [Assignment] = []
for a in parsed:
    if a.left.start <= a.right.start and a.left.end >= a.right.start:
        # Right starts in Left
        overlap.append(a)
    elif a.left.start <= a.right.end and a.left.end >= a.right.end:
        # Right ends in Left
        overlap.append(a)
    elif a.right.start <= a.left.start and a.right.end >= a.left.start:
        # Left starts in Right
        overlap.append(a)
    elif a.right.start <= a.left.end and a.right.end >= a.left.end:
        # Left ends in Right
        overlap.append(a)

for o in overlap:
    print(f"{o}")

print(f"Overlapping: {len(overlap)}")

