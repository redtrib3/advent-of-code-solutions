#!/usr/bin/python3

with open('input.txt','r') as f:
	fn = f.readlines()

payload = [i.strip('\n') for i in fn][0]

for i in range(len(payload)):
    if len(set(payload[i:i+4])) == 4:
        marker = i+4
        break
        	 
        	 
print(marker)   
