#!/usr/bin/python3

'''
    warning: is resource intensive (!), try converting ms to minutes approach.
             if program crashes. [!]
'''
import re

with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]


t_dist = []
for i in input:
    t_dist.append(''.join(re.findall(r'\d',i)))

time, distance = map(int, t_dist)

def no_of_ways(total_time: int, record_dist: int) -> int:

    wins = 0

    for i in range(1, total_time):
        dist_travelled = i * (total_time - i)

        if dist_travelled > record_dist:
            wins += 1

    return wins


all_ways = no_of_ways(time, distance)
print(all_ways)


