#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("\n Usage: ttt.py input_file \n\n")

fname = sys.argv[1];
with open(fname) as f:
        snacks = f.read().splitlines()

print(snacks)
elf = { "id": 1,
        "total_calories": 0,
        "snacks": [],
        }

elfs = []

for snack in snacks:
    if not snack:
        elfs.append(elf)
        # start a new elf
        elf = { "id": len(elfs)+1,
            "total_calories": 0,
            "snacks": [],
            }
    else:
        elf['total_calories'] += int(snack)
        elf['snacks'].append(snack)

max_calories = max(elfs, key=lambda x: x['total_calories'])
print(f"Top Elf has: {max_calories['total_calories']}")

max_cal_elfs = sorted(elfs, key=lambda x: x.get('total_calories'),reverse=True)
print(max_cal_elfs[0])
print(max_cal_elfs[1])
print(max_cal_elfs[2])

print(f"Sum of top three elfs: {(max_cal_elfs[0]['total_calories']+max_cal_elfs[1]['total_calories']+max_cal_elfs[2]['total_calories'])}")

