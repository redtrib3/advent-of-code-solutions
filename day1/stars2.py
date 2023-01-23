#!/usr/bin/python3
#https://adventofcode.com/2022/day/1/


# read elf's calorie data
with open('input','r') as f:
	ls = f.readlines()

# clean and convert to string
k = ''
for i in ls:
	k = k + i

ls = k.split("\n")



#c -counter for key value
c = 0
store = {}

#keep track of biggest sum
bigg = 0
for i in ls:
	try:
		bigg += int(i)
	except:
		c += 1
		key = f'e{c}'
		store[key] = bigg
		bigg = 0



allSums = []

for value in store:
	allSums.append(store[value])

p = 0
allSums.sort(reverse=True)

print(sum(allSums))
