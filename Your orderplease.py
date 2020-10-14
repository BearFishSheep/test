def order(sentence):
	if sentence == '':
		return ''
	s = sentence.split()
	ls = []
	ls1 = []
	for i in s:
		for j in i:
			if '1' <= j <= '9':
				ls.append(int(j))
				break
	ls = sorted(ls)
	for i in ls:
		for j in s:
			if str(i) in j:
				ls1.append(j)
	s1 = ' '.join(ls1)
	return s1
print(order("4of Fo1r pe6ople g3ood th5e the2"))