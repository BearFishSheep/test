def remove_smallest(numbers):
	ls = []
	if len(numbers) == 0:
		return ls
	a = 0
	for i in range(len(numbers)):
		if numbers[i] < numbers[a]:
			a = i
	for i in range(len(numbers)):
		if i != a:
			ls.append(numbers[i])
	return ls

print(remove_smallest([2,3,4,-1,5]))