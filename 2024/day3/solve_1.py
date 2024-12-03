import re

with open('input.txt','r') as f:
    input = f.read()

mul = lambda x,y: x*y

all_finds = re.findall(r'mul\(\d*,\d*\)', input)
print(sum([eval(i.strip()) for i in all_finds]))
