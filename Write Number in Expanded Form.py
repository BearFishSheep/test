def expanded_form(num):
	s = list(str(num))
	ls = []
	for i in range(len(s)):
		if int(s[i]):
			ls.append(str(int(s[i])*(10**(len(s)-i-1))))
	s1 = ' + '.join(ls)
	return s1
print(expanded_form(200001))