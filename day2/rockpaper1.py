#!/usr/bin/python3


def play(Omove,Pmove):

	state = ""

	#draw states
	if Omove == "A" and Pmove == "X":
		state = "draw"
	elif Omove == "B" and Pmove == "Y":
		state = "draw"
	elif Omove == "C" and Pmove == "Z":
		state = "draw"


	#win states
	if Omove == "A" and Pmove == "Y":
		state = "win"
	elif Omove == "B" and Pmove == "Z":
		state  = 'win'
	elif Omove == "C" and Pmove == "X":
		state = 'win'

	#lose states
	if Omove == "A" and Pmove == "Z":
		state = 'lose'
	elif Omove == "B" and Pmove == "X":
		state = 'lose'
	elif Omove == "C" and Pmove == "Y":
		state = 'lose'


	if state == 'win':
		return 6
	if state == 'draw':
		return 3
	if state == 'lose':
		return 0


with open("strategy","r") as f:
	p = f.readlines()


k = ''
for i in p:
	k = k + i

ls = k.split("\n")

#print(ls)

charPoints = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}


n = []
for j in ls:
	j = j.split()
	n.append(j)

#print(n)


score_store = []
for i in n:
    
    #discard empty lists
    
    if i:
        opp_move = i[0]
        my_move = i[1]
    
        round_score = play(opp_move, my_move)
        #print("roundscore=",round_score)
      
        shape_score = charPoints[my_move]
        #print("shapescore=",shape_score)
        
        total_rscore = round_score + shape_score
        #print("total=",total_rscore)
        #store all the scores
        score_store.append(total_rscore)
        

s = 0
for i in score_store:
    s = s + i
    
print(s)

#notes/Rules:
#In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a    score of 8 (2 because you chose Paper + 6 because you won).
#In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

