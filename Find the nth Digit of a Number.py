def find_digit(num, nth):
	num = abs(num)
	if nth <= 0:
		return -1
	s = list(str(num))
	if nth > len(s):
		return 0
	else:
		return int(s[len(s)-nth])
print(find_digit(-2825, 3))