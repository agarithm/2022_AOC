#!/usr/bin/python3

import sys
import pprint
from dataclasses import dataclass
from sys import getrefcount
print = pprint.pprint

if len(sys.argv) != 2:
    print("\n Usage: ttt.py input_file \n\n")

fname = sys.argv[1];
with open(fname) as f:
    commands = f.read().splitlines()

@dataclass
class file:
    name: str = ""
    size: int = 0

@dataclass
class dir:
    path: str
    dirs: []
    files: {}
    size: int = 0

root = dir(path="/", dirs=[], files={})
index: {str: dir}  = { "/": root}
cwd = root;


def changeDir(name):
    global cwd
    global root
    if name == "..":
        #up dir
        cwd = parent(cwd);
    elif name is "/":
        return root
    else:
        nextDir = cwd.path+"/"+name if cwd.path != "/" else "/"+name
        cwd = upsertDir(nextDir)

    #print(f"CD: {name} -> {cwd.path} ({getrefcount(cwd)})")

    


def upsertDir(path):
    if path in index:
        return index[path]

    # New directory
    pPath = parentPath(path)
    if pPath in index:
        parent = index[pPath]
    else:
        parent = upsertDir(pPath)

    index[path] = dir(path=path, dirs=[], files={})
    parent.dirs.append(index[path])
    return index[path]

def parentPath(cPath: str):
    path = "/".join(cPath.split("/")[:-1])
    if not path.startswith("/"):
        path = "/"+path;
    # print(f"Parent: {cPath} --> {path}");
    return path


def parent(d: dir):
    if d.path == '/':
        return d
    else:
        return upsertDir(parentPath(d.path))


def updateDirSize(d,size):
    d.size += int(size)
    if d.path == "/":
        return
    else:
        updateDirSize(parent(d),size)
    

def upsertFile(name,size):
    global cwd
    if name in cwd.files:
        return
    else:
        cwd.files[name] = file(name=name,size=int(size))
        updateDirSize(cwd,size)

for command in commands:
    parts = command.split(" ")
    if parts[0] == "$":
        # command
        if parts[1] == "cd":
            changeDir(parts[2])
        else:
            pass
    elif parts[0] == "dir":
        # directory found
        # Using side effect to populate the dir if missing, then back to original cwd
        changeDir(parts[1])
        changeDir("..")
    else:
        #file found
        upsertFile(parts[1],parts[0])


print(index,depth=1, width=200, indent=3)


total = 0;
for d in index:
    size = index[d].size
    if size <= 100000:
        total += size;

print(f"Total = {total}")

maxDisk = 70000000
used = index['/'].size
need = 30000000 - (maxDisk-used) 
print(f"{maxDisk},{used},{need}")

candidates = []
for d in index:
    size = index[d].size
    if size >= need:
        candidates.append(size)

candidates.sort()
print(f"{candidates[0]} or {candidates[len(candidates)-1]}")
        




