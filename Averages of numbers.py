def averages(arr):
	ls = []
	if arr == [] or arr == None:
		return ls
	for i in range(len(arr)-1):
		ls.append((arr[i]+arr[i+1])/2)
	return ls
print(averages([]))