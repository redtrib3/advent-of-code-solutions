#!/usr/bin/python3

with open('input.txt','r') as f:
    lines = [i.strip() for i in f.readlines()]

digit_final = []

for str in lines:
    nums = [i for i in str if i.isdigit()]
    digit = nums[0] + nums[-1]
    digit_final.append(digit)

print(sum(map(int, digit_final)))
