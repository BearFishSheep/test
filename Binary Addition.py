def add_binary(a, b):
	s = ''
	c = a + b
	ls = []
	while c:
		ls.append(c % 2)
		c = int(c / 2)
	i = len(ls) - 1
	while i >= 0:
		s = s + str(ls[i])
		i -= 1
	return s
print(add_binary(238410294836016026, 96971731830802321))