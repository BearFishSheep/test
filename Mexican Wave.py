def wave(s):
	ls = []
	if len(s) == 0:
		return ls
	ls1 = list(s)
	for i in range(len(ls1)):
		s1 = ''
		for j in range(len(ls1)):
			if j != i:
				s1 += ls1[j]
			elif j == i and 'a' <= ls1[i] <= 'z' and 'a' <= ls1[j] <= 'z':
				s1 += ls1[j].upper()
		for k in s1:
			if 'A' <= k <= 'Z':
				ls.append(s1)
	return ls
print(wave(' this  is a  few words'))