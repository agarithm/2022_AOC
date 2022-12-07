#!/usr/bin/python3

import sys
import pprint
from dataclasses import dataclass
from queue import LifoQueue


if len(sys.argv) != 2:
    print("\n Usage: ttt.py input_file \n\n")

fname = sys.argv[1];
with open(fname) as f:
        lines = f.read().splitlines()


# Parse Starting State
raw_stack = LifoQueue()
row = lines.pop(0);
while row:
    raw_stack.put(row)
    row = lines.pop(0);
    print(row)


col_labels = raw_stack.get();
col_names = ['1','2','3','4','5','6','7','8','9']
col_positions = [];
cols = {}

print(f"Labels: {col_labels}")
for i in col_names:
    pos = col_labels.rfind(i);
    col_positions.append(pos)
    cols[i]=LifoQueue()
    print(f"{i} = {col_positions}")

while not raw_stack.empty():
    row = list(raw_stack.get())
    for i in col_names:
        pos = col_labels.rfind(i);
        val = row[pos]
        if val != ' ':
            cols[i].put(val)

for i in col_names: 
    print(f"{i} = {cols[i].qsize()}", end=" ")
    #while not cols[i].empty():
        # print(f"{cols[i].get()}",end="")
    print("")

for line in lines:
    parts = line.split(" ")
    end = int(parts[1])
    here = str(parts[3])
    there = str(parts[5])
    for x in range(end):
        item = cols[here].get()
        cols[there].put(item)

for i in col_names: 
    print(f"{i} = {cols[i].qsize()}", end=" ")
    while not cols[i].empty():
         print(f"{cols[i].get()}",end="")
    print("")


print("##################################################")

fname = sys.argv[1];
with open(fname) as f:
        lines = f.read().splitlines()


# Parse Starting State
raw_stack = LifoQueue()
row = lines.pop(0);
while row:
    raw_stack.put(row)
    row = lines.pop(0);
    print(row)


col_labels = raw_stack.get();
col_names = ['1','2','3','4','5','6','7','8','9']
col_positions = [];
cols = {}

print(f"Labels: {col_labels}")
for i in col_names:
    pos = col_labels.rfind(i);
    col_positions.append(pos)
    cols[i]=LifoQueue()
    print(f"{i} = {col_positions}")

while not raw_stack.empty():
    row = list(raw_stack.get())
    for i in col_names:
        pos = col_labels.rfind(i);
        val = row[pos]
        if val != ' ':
            cols[i].put(val)

for i in col_names: 
    print(f"{i} = {cols[i].qsize()}", end=" ")
    #while not cols[i].empty():
        # print(f"{cols[i].get()}",end="")
    print("")

for line in lines:
    parts = line.split(" ")
    end = int(parts[1])
    here = str(parts[3])
    there = str(parts[5])

    items=[]
    for x in range(end):
        items.append(cols[here].get())
    for x in range(end):
        cols[there].put(items.pop())


for i in col_names: 
    print(f"{i} = {cols[i].qsize()}", end=" ")
    while not cols[i].empty():
         print(f"{cols[i].get()}",end="")
    print("")


