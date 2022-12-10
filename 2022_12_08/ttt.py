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
    rows = f.read().splitlines()

trees = []
for row in rows:
    trees.append(list(row))

def paint(g):
    for x in range(0,max_x):
        for y in range(0,max_y):
            print(g[x][y],end=" ")
        print(" ")


def grid(x,y):
    out = []
    for i in range(0,x):
        row = []
        for j in range(0,y):
            row.append(0)
        out.append(row)
    return out

max_x = len(trees)
max_y = len(trees[0])

up = grid(max_x,max_y);
down = grid(max_x,max_y);
left = grid(max_x,max_y);
right = grid(max_x,max_y);
visible = grid(max_x,max_y);

# Normalize Up / Left
for x in range(0,max_x):
    for y in range(0,max_y):
        tree = int(trees[x][y])
        u = int(up[x][y-1]) if (y-1) >= 0 else -1 
        l = int(left[x-1][y]) if (x-1) >= 0 else -1 
        d = int(down[x][y+1]) if (y+1) < max_y else -1 
        r = int(right[x+1][y]) if (x+1) < max_x else -1 

        if u < tree:
            up[x][y] = tree
            visible[x][y] += 1
        else:
            up[x][y] = +up[x][y-1]

        if l < tree:
            left[x][y] = tree
            visible[x][y] += 1
        else:
            left[x][y] = +left[x-1][y]

# Normalize down / right
for x in range(max_x-1,-1,-1):
    for y in range(max_y-1,-1,-1):
        tree = int(trees[x][y])
        u = int(up[x][y-1]) if (y-1) >= 0 else -1 
        d = int(down[x][y+1]) if (y+1) < max_y else -1 
        r = int(right[x+1][y]) if (x+1) < max_x else -1 
        l = int(left[x-1][y]) if (x-1) >= 0 else -1 

        if d < tree:
            down[x][y] = tree
            visible[x][y] += 1
        else:
            down[x][y] = +down[x][y+1]

        if r < tree:
            right[x][y] = tree
            visible[x][y] += 1
        else:
            right[x][y] = +right[x+1][y]


paint(visible)

print("###### UP ######")
paint(up)
print("")

print("###### DOWN ######")
paint(down)
print("")

print("###### LEFT ######")
paint(left)
print("")

print("###### RIGHT ######")
paint(right)
print("")

visibleCount = 0
for x in range(0,max_x):
    for y in range(0,max_y):
        if visible[x][y] > 0:
            visibleCount += 1

print(f"Visible Trees: {visibleCount}")

##########################################################
up = grid(max_x,max_y);
down = grid(max_x,max_y);
left = grid(max_x,max_y);
right = grid(max_x,max_y);

def treesUp(x,y):
    global trees
    out = 1
    tree = int(trees[x][y])
    height = 0 
    if y == 0:
        return 0
    else:
        for i in range(y-1,0,-1):
            if int(trees[x][i]) < tree and int(trees[x][i]) >= height:
                out += 1
                height = max(height,int(trees[x][i])) 
            elif int(trees[x][i]) < tree:
                out += 1
                pass
            else:
                return out
    return out

def treesLeft(x,y):
    global trees
    out = 1
    height = 0 
    tree = int(trees[x][y])
    if x == 0:
        return 0
    else:
        for i in range(x-1,0,-1):
            if int(trees[i][y]) < tree and int(trees[i][y]) >= height:
                out += 1
                height = max(height,int(trees[i][y])) 
            elif int(trees[i][y]) < tree:
                out += 1
                pass
            else:
                return out
    return out

def treesRight(x,y):
    global trees
    global max_x, max_y
    out = 1
    height = 0 
    tree = int(trees[x][y])
    if x == max_x-1:
        return 0
    else:
        for i in range(x+1,max_x-1):
            if int(trees[i][y]) < tree and int(trees[i][y]) >= height:
                out += 1
                height = max(height,int(trees[i][y])) 
            elif int(trees[i][y]) < tree:
                out += 1
                pass
            else:
                return out
    return out

def treesDown(x,y):
    global trees
    global max_x, max_y
    height = 0 
    out = 1
    tree = int(trees[x][y])
    if y == max_y-1:
        return 0
    else:
        for i in range(y+1,max_y-1):
            if int(trees[x][i]) < tree and int(trees[x][i]) >= height:
                out += 1
                height = max(height,int(trees[x][i])) 
            elif int(trees[x][i]) < tree:
                out += 1
                pass
            else:
                return out
    return out

# Count in all directions
max_view = 0
view = grid(max_x,max_y)
for x in range(0,max_x):
    for y in range(0,max_y):
        up[x][y] = treesUp(x,y)
        left[x][y] = treesLeft(x,y)
        right[x][y] = treesRight(x,y)
        down[x][y] = treesDown(x,y)

        view[x][y] = up[x][y] * down[x][y] * left[x][y] * right[x][y]
        max_view = max(max_view,view[x][y])


paint(view)

print(max_view)

print(f"up = {treesUp(98,1)}")
print(f"down = {treesDown(98,1)}")
print(f"left = {treesLeft(98,1)}")
print(f"right = {treesRight(98,1)}")
print("")
print(f"up = {treesUp(97,0)}")
print(f"down = {treesDown(97,0)}")
print(f"left = {treesLeft(97,0)}")
print(f"right = {treesRight(97,0)}")
print("")
print(f"up = {treesUp(95,0)}")
print(f"down = {treesDown(95,0)}")
print(f"left = {treesLeft(95,0)}")
print(f"right = {treesRight(95,0)}")
