def find_smallest(numbers, to_return):
	if to_return == 'value':
		return min(numbers)
	else:
		m = min(numbers)
		for i in range(len(numbers)):
			if numbers[i] == m:
				return i
print(find_smallest([5,4,3,2,1],"index"))