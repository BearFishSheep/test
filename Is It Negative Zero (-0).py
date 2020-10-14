def is_negative_zero(n):
	s = str(n)
	if s[0] == '-' and n == 0:
		return True
	else:
		return False
print(is_negative_zero(0.0))