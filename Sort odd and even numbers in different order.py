def sort_array(s):
	a = []
	y, z= 0, 0
	c = []
	d = []
	if s == []:
		return s
	for i in s:
		if i % 2:
			a.append(i)
		else:
			d.append(i)
	a = sorted(a)
	d = sorted(d, reverse = True)
	for i in s:
		if i % 2:
			c.append(a[y])
			y += 1
		else:
			c.append(d[z])
			z += 1
	return c
print(sort_array([5, 3, 2, 8, 1, 4]))