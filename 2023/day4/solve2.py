#!/usr/bin/python3

with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]

winning_nums = []
curr_nums = []
N = len(winning_nums)

points = [pow(2,i) for i in range(10)]

for i in input:
    snums = i.split(':')[1].split('|')
    winning_nums.append(list(map(int,snums[0].split())))
    curr_nums.append(list(map(int,snums[1].split())))

# get the number for wins by game
def get_wins(game_no):
    global winning_nums,curr_nums
    w = winning_nums[game_no]
    c = curr_nums[game_no]
    wins = []
    for i in w:
        if i in c:
            wins.append(i)

    return len(wins)

#store the winnings for each game
copies = [[] for _ in range(N)]

# store the copies
for i in range(N):
    no_of_wins = get_wins(i)

    for j in range(i+1, i+no_of_wins+1):
        copies[i].append(j)


score = [1 for _ in range(N)]

for i in range(N-1, -1, -1):
    for j in copies[i]:
        score[i] += score[j]

print(sum(score))
