from re import match
f = open('input.txt')

dictionaries = []
seeds = match(r'seeds: (.+)', f.readline())
seeds = list(map(int, seeds.group(1).split()))

print(seeds)

all_seeds = []
for i in range(len(seeds)-1):
    seed_val = seeds[i]
    seed_rng = seeds[i+1]
    all_seeds.append([_ for _ in range(seed_val, seed_val+seed_rng)])


while k := f.readline():
    if k == '\n':
        dictionaries.append({})
        continue
    k = k.strip('\n')
    res = match(r'(\d+) (\d+) (\d+)', k)
    if not res: continue
    dest,start,breadth = map(int, res.groups())
    dictionaries[-1][(start,start+breadth-1)] = dest

n = len(dictionaries)
locations = []
for seed in seeds:
    i = 0
    k = seed
    while i < n:
        for a,b in dictionaries[i]:
            if not a <= k <= b: continue
            delta = k - a
            k = dictionaries[i][a,b] + delta
            break
        i += 1
    locations.append(k)

print(locations)
