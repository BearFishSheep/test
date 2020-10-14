def two_sum(numbers, target):
	ls = []
	for i in range(0, len(numbers)-1):
		for j in range(i+1, len(numbers)):
			if numbers[i]+numbers[j]==target:
				ls.append(i)
				ls.append(j)
				return ls
print(two_sum([2,2,3], 4))