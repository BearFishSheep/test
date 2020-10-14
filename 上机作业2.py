nums=[2, 7, 11, 15, 1, 8, 7, 3, 4, 6, 5]
i= 0
ls=list()
while i< 11:
	j= i+1
	while j< 11:
		if nums[i]+nums[j] == 9:
			ls.append((i, j))
		j+= 1
	i+= 1
print(ls)