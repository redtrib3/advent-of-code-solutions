#!/usr/bin/env python3

# read the input

with open('input.txt', 'r') as f:
    lines = [i.strip() for i in f.readlines()]

left = []
right = []

for i in lines:
    l, r = i.split()
    left.append(int(l))
    right.append(int(r))

left = sorted(left)
right = sorted(right)

final_sum = 0
for i in range(len(left)):
    diff = max(left[i], right[i]) - min(left[i], right[i])
    final_sum += diff

print(final_sum)
