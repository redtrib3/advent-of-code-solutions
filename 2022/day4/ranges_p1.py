
with open('input.txt','r') as f:
    s = f.readlines()

range_list = []   
for i in s:
    i = i.replace('\n','')
    range_list.append(i)


def isRangeOverlapping(range1,range2):
    start_a, end_a = map(int,range1.split('-'))
    start_b, end_b = map(int,range2.split('-'))
    return start_b <= start_a and end_a <= end_b


c = 0
for ranges in range_list:
    fi_range,se_range = ranges.split(',')  
    
    
    #[ j for j in range(int([i.split('-') for i in ranges ][0][0]),int([i.split('-') for i in ranges ][0][1])+1) ]
    #elf1_range = range(int([i.split('-') for i in ranges ][0][0]),int([i.split('-') for i in ranges ][0][1])+1)
    #elf2_range = range(int([i.split('-') for i in ranges ][1][0]),int([i.split('-') for i in ranges ][1][1])+1)
    #xs = set(elf1_range)
    #shared_nums = xs.intersection(elf2_range)

    if isRangeOverlapping(fi_range,se_range) or isRangeOverlapping(se_range, fi_range):
        c += 1   
        
print(c)
