#!/usr/bin/python3

# Highly unoptimized and resource intesive code below!
# best used with sample data only.(or if you own >=16GB ram machine)

with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]

input = [i for i in input if i]

seeds = input.pop(0).split(':')[1].split()
seeds = list(map(int, seeds))

print("[+]","Generated seeds")


maps = {}
temp = []
curr_key = ''

j = 0
while (j < len(input)):
    p = input[j]

    if 'to' in p:
        if j!=0:
            maps[curr_key.replace(':','')] = temp
            curr_key = p
            temp = []
        else:
            curr_key = p
    else:
       temp.append(list(map(int,p.split())))

    j+=1

#add last key too
maps[curr_key.replace(':','')] = temp
curr_key = p

print("[~]","creating maps")
all_maps = {}
for i in maps:
    src_dst_map = {}
    for line in maps[i]:
        dst, src, range_no = line
        src_range = [ _ for _ in range(src, src+range_no)]
        dst_range = [ _ for _ in range(dst, dst+range_no)]

        for x,y in zip(src_range, dst_range):
            src_dst_map[x] = y


    all_maps[i] = src_dst_map

print("[+]","Created all maps...")
print("[~]","Starting to find locations")

locations = []
for seed in seeds:
    next_loc = seed
    for i in all_maps:
        try:
            next_loc =  all_maps[i][next_loc]
        except:
            continue

    locations.append(next_loc)

#print(locations)

print(min(locations))
