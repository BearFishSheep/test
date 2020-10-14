def high_and_low(numbers):
	s = numbers.split()
	ls = []
	for i in s:
		ls.append(int(i))
	s1 = ''
	s1 = s1 + str(max(ls)) + ' ' + str(min(ls))
	return s1

print(high_and_low("1 9 3 4 -5"))