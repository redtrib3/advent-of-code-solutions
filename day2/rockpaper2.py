#!/usr/bin/python3

def  weaponPoints(opp_shape, game_var):

    pts = {"rock":1,"paper":2,"scissor":3}

    if game_var == "Z":
    
        if opp_shape == 'A':
            our_points = pts['paper']
        elif opp_shape == 'B':
            our_points = pts['scissor']
        elif opp_shape == 'C':
            our_points = pts['rock']
             
    if game_var == "Y":
        
        if opp_shape == 'A':
            our_points = pts['rock']
        elif opp_shape == 'B':
            our_points = pts['paper']
        elif opp_shape == 'C':
            our_points = pts['scissor']

    if game_var == "X":
        
        if opp_shape == 'A':
            our_points = pts['scissor']
        elif opp_shape == 'B':
            our_points = pts['rock']
        elif opp_shape == 'C':
            our_points = pts['paper']

    return our_points

with open("strategy","r") as f:
	p = f.readlines()

print("\n>>>>>>>>>STEP:1\n")
print(p)

k = ''
for i in p:
	k = k + i

ls = k.split("\n")

print("\n>>>>>>>>>>>STEP:2\n")
print(ls)
#print(ls)

#charPoints = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}
gamePoints = {"X":6,"Y":3,"Z":0}


n = []
for j in ls:
	j = j.split()
	n.append(j)

print("\n>>>>>>>>>>>STEP:3\n")
print(n)

s = 0
for i in n:

    if i:
        opp_shape = i[0]
        g = i[1]
    
        game_point = gamePoints[g]    
        weapon_point = weaponPoints(opp_shape,g)
        
        tPoints = game_point + weapon_point
        s = s + tPoints
        
print("SUM of points = ",s)    
        
    
    
