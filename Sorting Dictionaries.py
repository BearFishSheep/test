def sort_dict(d):
	ls = []
	s = list(d.items())
	for i in range(len(s)-1):
		j, k = s[i]
		m = i
		m2 = k
		for t in range(i+1, len(s)):
			t1, t2 = s[t]
			if t2 > m2:
				m = t
				m2 = t2
		if m != i:
			s[m], s[i] = s[i], s[m]
	for i in s:
		ls.append(i)
	return ls
print(sort_dict({1:2, 2:3, -1:9, 4:10, 3:5}))