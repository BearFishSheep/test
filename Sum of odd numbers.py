def row_sum_odd_numbers(n):
	sum = 0
	t = n * (n-1) + 1
	for i in range(n):
		sum += t
		t += 2
	return sum
print(row_sum_odd_numbers(2))