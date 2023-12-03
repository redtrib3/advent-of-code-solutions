#!/usr/bin/python3

with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]


total_rows = len(input)
total_cols = len(input[0])

star_store = [[[] for _ in range(total_cols)] for _ in range(total_rows)]

def is_symbol(i, j, num):

    if not (0 <= i < total_rows and 0 <= j < total_cols):
        return False

    if input[i][j] == '*':
        star_store[i][j].append(num)

    return input[i][j] != '.' and not (input[i][j].isdigit())


final = 0

for index, line in enumerate(input):
    start = 0
    curr_pos = 0

    while (curr_pos < total_cols):
        start = curr_pos
        num = ""

        while curr_pos < total_cols and line[curr_pos].isdigit():
            num += line[curr_pos]
            curr_pos += 1

        if num == "":
            curr_pos+=1
            continue

        num = int(num)

        is_symbol(index, start-1, num) or is_symbol(index, curr_pos, num)

        for char_idx in range(start-1, curr_pos+1):
            is_symbol(index-1, char_idx, num)  or is_symbol(index+1, char_idx, num)

print(star_store)

for i in range(total_rows):
    for j in range(total_cols):
        nums = star_store[i][j]
        if nums:
            if input[i][j] == '*' and len(nums) == 2:
                final += nums[0]*nums[1]

print(final)
