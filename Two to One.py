def longest(s1, s2):
	ls = list(s1 + s2)
	s = set(ls)
	ls1 = list(s)
	ls1.sort()
	s1 = ''.join(ls1)
	return s1
print(longest("aretheyhere", "yestheyarehere"))