#!/usr/bin/python3

with open('input.txt','r') as f:
    input = f.read()

time, distance = [list(map(int,i.split(':')[1].strip().split())) for i in input.splitlines()]
time_dist = list(zip(time,distance))


def no_of_ways(total_time: int, record_dist: int) -> int:

    win = []
    t = total_time

    for i in range(1, total_time):
        dist_travelled = i * (t - i)

        if dist_travelled > record_dist:
            win.append(i)

    return len(win)


s = 1
for total_time, rec_dist in time_dist:
    all_ways = no_of_ways(total_time, rec_dist)
    s *= all_ways


print(s)
