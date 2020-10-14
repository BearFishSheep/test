def binary_array_to_number(arr):
	a, i = 0, 0
	k = len(arr) - 1
	while k >= 0:
		a += arr[k] * (2**i)
		k -= 1
		i += 1
	return a

print(binary_array_to_number([1, 0, 0, 1, 1]))