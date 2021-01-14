#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet
# Debug Info
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
#

# MEMORY
# /bin/free not working for ubuntu, swapped for free -m, check if output right
# MEMORY: seems to have a problem with size conversion, shows 3.7kib instead of gib
raw_free = run_cmd("free -m").split("\n")
raw_mem = raw_free[1].split()
raw_swap = raw_free[2].split()
# MEMORY: puts memorydata and ratio in array 
memory = {'used': int(raw_mem[1])-int(raw_mem[2]),
            'total': int(raw_mem[1])}
memory['ratio'] = float(memory['used'])/memory['total']
# MEMORY: same as above for swap
swap = {'used': int(raw_swap[2]),
        'total': int(raw_swap[1])}
swap['ratio'] = 0.0 if swap['total'] == 0 else float(swap['used'])/swap['total']
