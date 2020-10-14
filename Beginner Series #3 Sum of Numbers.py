def get_sum(a, b):
	if a > b:
		a, b = b, a
	t = 0
	for i in range(a, b+1):
		t += i
	return t

print(get_sum(-1, -1))