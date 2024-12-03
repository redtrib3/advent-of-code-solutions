#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = [i.strip() for i in f.readlines()]

lvls = []
for line in lines:
    lvls.append(list(map(int, line.split())))

# find if the list is valid-increasing or decreasing only.
def is_incr_or_decr(level):
    increasing = all(level[i] < level[i+1] for i in range(len(level)-1))
    decreasing = all(level[i] > level[i+1] for i in range(len(level)-1))

    if increasing or decreasing:
        return True
    return False

def is_safe(level):

    if not is_incr_or_decr(level):
        return False

    for i in range(len(level)-1):

        adj_diff = abs(level[i] - level[i+1])
#        print(level,f'{level[i]}, adj_diff= {adj_diff}')

        if adj_diff not in [1,2,3]:
            return False

    return True

safe_lvls = 0

for lvl in lvls:
    if is_safe(lvl):
        safe_lvls += 1

print(safe_lvls)
