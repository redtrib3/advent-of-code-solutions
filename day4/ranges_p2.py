
with open('input.txt','r') as f:
    s = f.readlines()

range_list = []
for i in s:
    i = i.replace('\n','')
    range_list.append(i)


count = 0
for ranges in range_list:
	first_range,sec_range = ranges.split(',')
	f_range_nums = first_range.split('-')
	s_range_nums = sec_range.split('-')

	elf1_range =  range(int(f_range_nums[0]), int(f_range_nums[1])+1)
	elf2_range =  range(int(s_range_nums[0]), int(s_range_nums[1])+1)

	elf1set = set(elf1_range)
	elf2set  = set(elf2_range)

  #check if the overlapping set is not empty 
	if elf1set.intersection(elf2set):
		count += 1

print(count)
