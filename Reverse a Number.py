def reverse_number(n):
	if n >= 0:
		t = 0
		while n:
			t = n%10 + t*10
			n = int(n / 10)
	else:
		n = n*(-1)
		t = 0
		while n:
			t = n%10 + t*10
			n = int(n / 10)
		t = t*(-1)
	return t

print(reverse_number(123))