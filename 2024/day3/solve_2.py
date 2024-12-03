import re

with open('input.txt','r') as f:
    input = f.read()

mul = lambda x,y: x*y

all_finds = re.findall(r'mul\(\d*,\d*\)|don\'t\(\)|do\(\)', input)
#print(all_finds)

do = 1
final_res = 0
for i in all_finds:

    if i == "don\'t()":
        do = 0
        continue

    if i == "do()":
        do = 1
        continue

    if do:
        final_res += eval(i)
        continue


print(final_res)
