def mergeArrays(arr1, arr2):
	arr = arr1 + arr2
	s = set(arr)
	arr = list(s)
	arr.sort()
	#或者arr = sorted(arr)
	return arr

a = [1,2,3,5]
b = [5,6,7,8]
print(mergeArrays(a,b))