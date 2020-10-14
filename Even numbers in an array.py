def even_numbers(arr, n):
	ls = []
	cnt = 0
	i = len(arr) - 1
	while i >= 0:
		if cnt < n and arr[i] % 2 == 0:
			ls.append(arr[i])
			cnt += 1
		i -= 1
	ls.reverse()
	return ls
print(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2))