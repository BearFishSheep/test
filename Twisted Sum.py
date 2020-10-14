def compute_sum(n):
	if n < 10:
		sum = 0
		for i in range(1, n+1):
			sum += i
	else:
		sum = 45
		for i in range(10, n+1):
			t = i
			while t:
				sum += t%10
				t = int(t/10)
	return sum
print(compute_sum(11))