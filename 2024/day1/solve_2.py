#!/usr/bin/env python3

with open("input.txt", 'r') as f:
    lines = [i.strip() for i in f.readlines()]

left = []
right = []

for i in lines:
    l, r = i.split()
    left.append(int(l))
    right.append(int(r))


similarity_score = 0
for i in range(len(left)):
    score = left[i] * right.count(left[i])
    similarity_score += score

print(similarity_score)

