#!/usr/bin/python3

import sys
from dataclasses import dataclass

if len(sys.argv) != 2:
    print("\n Usage: ttt.py input_file \n\n")

fname = sys.argv[1];
with open(fname) as f:
    signals = list(f.read())


def validMarker(marker):
    temp = {}
    for x in marker:
        if x in temp:
            return False
        else:
            temp[x]=x;
    return True

def indexOfStart(msg,delLength=4):
    out = -1;
    start = delLength;
    while start < len(msg):
        marker = msg[start-delLength:start]
        print(f"{marker}");
        if(validMarker(marker)):
            return start
        else:
            start += 1


firstPacket = indexOfStart(signals);
print(f"First packet @ {firstPacket}")

firstMsg = indexOfStart(signals,14);
print(f"First message @ {firstMsg}")
