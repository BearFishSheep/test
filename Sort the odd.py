def sort_array(s):
	a = []
	x, y = 0, 0
	c = []
	if s == []:
		return s
	for i in s:
		if i % 2:
			a.append(i)
			x += 1
	a = sorted(a)
	for i in s:
		if i % 2:
			c.append(a[y])
			y += 1
		else:
			c.append(i)
	return c
print(sort_array([5, 3, 1, 8, 0]))