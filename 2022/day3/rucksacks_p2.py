
# getting input and sanitizing it

rs_list = []
with open("input.txt", 'r') as f:
    fc = f.readlines()

for i in fc:
    i = i.replace("\n", '')
    rs_list.append(i)

#creating groups of 3
rs_groups = []
for i in range(0,len(rs_list),3):
    group = rs_list[i:i+3]
    rs_groups.append(group)
    

# creating a priority list from aA-zZ (1-52)
priority_ls = {}

lchars = "@abcdefghijklmnopqrstuvwxyz"
uchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

chars = lchars + uchars

for i in range(1, 53):
    p = chars[i]
    priority_ls[p] = i

#print(priority_ls)
    

def findCommon(group):
    x = ''
    comm = set.intersection(*map(set,group))
    for c in comm:
        x = x+c
    return c
    
commList = []
for i in rs_groups:
    common = findCommon(i)
    commList.append(common)
    
counter = 0
for i in commList:
    val = priority_ls[i]
    counter += val

print(counter)

