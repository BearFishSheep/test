def min_value(digits):
	s = list(set(digits))
	s.sort()
	t = 0
	for i in range(len(s)):
		t += s[i]*(10**(len(s)-i-1))
	return t
print(min_value([4, 8, 1, 4]))