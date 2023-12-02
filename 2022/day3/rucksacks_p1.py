#!/usr/bin/python3

# getting input and sanitizing it

rs_list = []
with open("input.txt", 'r') as f:
    fc = f.readlines()

for i in fc:
    i = i.replace("\n", '')
    rs_list.append(i)

# creating a priority list from aA-zZ (1-52)
priority_ls = {}

lchars = "@abcdefghijklmnopqrstuvwxyz"
uchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

chars = lchars + uchars

for i in range(1, 53):
    p = chars[i]
    priority_ls[p] = i

#print(priority_ls)

def findCommon(c1, c2):
    c = ''
    for i in c1:
        if i in c2:
            if i not in c:
                c = i
    return c

commons = []

for i in rs_list:
    length = int(len(i)/2)  # dividing by compartment
    comp1 = i[:length]
    comp2 = i[length:]

    common = findCommon(comp1, comp2)
    commons.append(common)

count = 0
for i in commons:
    val = priority_ls[i]
    count = count + val

print("priority count =",count)
