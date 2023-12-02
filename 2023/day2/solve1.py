#!/usr/bin/python3


# taking input
with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]


# cleaning: divide by games:
# {'game':[[('noset1','colorset1'), ('noset1','colorset1')],[('noset2','colorset2')...], 'game':[[..],[..],...]...}

d = {}
for i in input:
    j = i.split(':')
    d[j[0].split()[1]] = [p.strip().split(',') for p in j[1].strip().split(';')]

for game in d.keys():
    t = []
    for sets in d[game]:
        t.append([tuple(i.strip().split()) for i in sets])
    d[game] = t

#print(d)

# PROCESS

MAX_BALLS = {"red":12, "green":13, "blue":14}
VALID_GAMES = []

for game in d.keys():
    IS_VALID = True
    for sets in d[game]:
        for i in sets:
            if int(i[0]) > MAX_BALLS[i[1]]:
                IS_VALID = False
    if IS_VALID:
        VALID_GAMES.append(game)

#print(VALID_GAMES)
final = sum(map(int, VALID_GAMES))
print(final)
