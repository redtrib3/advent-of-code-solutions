#!/usr/bin/python3

with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]


# number of lines/rows
total_rows = len(input)
# number of chars/cols
total_cols = len(input[0])



# returns if a characters in cord is a symbol or not
def is_symbol(i, j):

    # if the supplied coordinates are not within bounds
    if not (0 <= i < total_rows and 0 <= j < total_cols):
        return False

    return input[i][j] != '.' and not (input[i][j].isdigit())


final = 0

for index, line in enumerate(input):
    start = 0
    curr_pos = 0

    # iterate while the curr characters is within bounds.
    while (curr_pos < total_cols):
        start = curr_pos
        num = ""

        # while the curr char is within bounds and is a digit
        while curr_pos < total_cols and line[curr_pos].isdigit():
            #store that digit to num
            num += line[curr_pos]
            curr_pos += 1

        # if the curr char is not a digit, num will be empty, move on to next line
        if num == "":
            curr_pos+=1
            continue

        num = int(num)

        # check if left OR right char is a symbol
        # here index is the current row number. start is the copy of curr_pos
        if is_symbol(index, start-1) or is_symbol(index, curr_pos):
            final += num
            continue

        # iterate characters from start of the number - 1th pos to end of number + 1th
        # the start-1 to check start diagonals, curr_pos i.e end+1 to check end diagonals
        for char_idx in range(start-1, curr_pos+1):

            # check if the char just above row or below row is a symbol
            if is_symbol(index-1, char_idx)  or is_symbol(index+1, char_idx):
                final += num
                break

print(final)
