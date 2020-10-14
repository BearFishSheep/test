def get_length_of_missing_array(arr):
	ls = []
	if arr == []:
		return 0
	for i in arr:
		if i == None:
			return 0
		else:
			ls.append(len(i))
	ls = sorted(ls)
	for i in range(len(ls)-1):
		if(ls[i+1] - ls[i] != 1):
			return (ls[i]+1)
print(get_length_of_missing_array([None, [None, None, None]]))