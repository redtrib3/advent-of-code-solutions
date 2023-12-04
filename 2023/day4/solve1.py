#!/usr/bin/python3

with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]

winning_nums = []
curr_nums = []

# each wins doubles [1,2,4,8,16...]
points = [pow(2,i) for i in range(10)]

for i in input:
    snums = i.split(':')[1].split('|')
    winning_nums.append(list(map(int,snums[0].split())))
    curr_nums.append(list(map(int,snums[1].split())))

# can have repeating nums in two sets, so intersection is not possible
# set(winning_nums[0]).intersection(set(curr_nums[0]))


curr_points = 0

for i in range(len(winning_nums)):
    wins = []
    for j in range(len(winning_nums[i])):
        if winning_nums[i][j] in curr_nums[i]:
            wins.append(winning_nums[i][j])

#    print(f"set-{i+1}",wins)
#    an empty wins[] adds highest point since len -1 is =-1
    if wins:
        curr_points += points[len(wins)-1]


print(curr_points)

