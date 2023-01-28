with open('input.txt','r') as f:
	x = f.readlines()

x = [i.strip('\n') for i in x]

cmds = x[x.index('')+1:]

crates = [
    ['V','Q','W','M','B','N','Z','C'],
    ['B','C','W','R','Z','H'],
    ['J','R','Q','F'],
    ['T','M','N','F','H','W','S','Z'],
    ['P','Q','N','L','W','F','G'],
    ['W','P','L'],
    ['J','Q','C','G','R','D','B','V'],
    ['W','B','N','Q','Z'],
    ['J','T','G','C','F','L','H']

]

for cmd in cmds:

    cmdDiv = cmd.split()
    
    qty = int(cmdDiv[1])
    from_crate = int(cmdDiv[3]) - 1
    to_crate = int(cmdDiv[5])   - 1
    
    move_this = crates[from_crate][:qty]
    del crates[from_crate][:qty]

    #extend to the start of a list
    if qty == 1:
        for elements in move_this:
            crates[to_crate].insert(0,elements)
    else:
        crates[to_crate] = move_this + crates[to_crate]
        
x = ''
for i in crates:
    end = i[0]
    x = x + end
    
print(x)
