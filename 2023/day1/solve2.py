#!/usr/bin/python3

import re

k = {
    'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10
    }

with open('input.txt','r') as f:
    strings = [i.strip() for i in f.readlines()]


# match all digits pattern
pattern = '|'.join(k.keys()) + '|' + r'\d'

final = 0
for i in strings:
    p,l = [],[]

    all_matches = []
    #match all string digits
    match_dig = re.findall(pattern, i)

    # extract the first and last digits
    p.extend([match_dig[0],match_dig[-1]])

    # convert all digits to integers, ints remain integers
    for j in p:
        try:
            l.append(int(j))
        except:
            l.append(k[j])

    final += int(''.join(str(dig) for dig in l))

    #print(i, ':', l)

print(final_sum)
