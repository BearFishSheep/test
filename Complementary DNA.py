def DNA_strand(s):
	#字符串具有不能更改的性质，所以将其先转化为列表,
	#对列表进行完修改后再把列表用join的方法连接成字符串
	ls = list(s)
	ls1 = []
	for i in ls:
		if i == 'A':
			ls1.append('T')
		if i == 'T':
			ls1.append('A')
		if i == 'C':
			ls1.append('G')
		if i == 'G':
			ls1.append('C')
	s1 = ''.join(ls1)
	return s1
print(DNA_strand('GTAT'))