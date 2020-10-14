def stray(arr):
	s = set(arr)
	for i in s:
		if arr.count(i) == 1:
			return i

print(stray([1,1,2,1]))