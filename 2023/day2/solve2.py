

with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]

def mul_list(x: list)->int:
    p = 1
    for i in x:
        p = p * i
    return p

#st = {'red':0,'green':0,'blue':0}


d = {}
for i in input:
    j = i.split(':')
    d[j[0].split()[1]] = [p.strip().split(',') for p in j[1].strip().split(';')]

#print(d)

x = {}
for i in d.keys():
    p = []
    for j in d[i]:
        p.extend([k.strip() for k in j])
    x[i] = p

#print(x)
m = 0
for i in d.keys():
    red,green,blue= [],[],[]
    subset = x[i]
    red.extend([int(j.split()[0]) for j in subset if 'red' in j])
    green.extend([int(j.split()[0]) for j in subset if 'green' in j])
    blue.extend([int(j.split()[0]) for j in subset if 'blue' in j])

    m += mul_list([max(red),max(green),max(blue)])

print(m)
