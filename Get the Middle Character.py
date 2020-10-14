def get_middle(s):
	s1 = ''
	k = len(s)
	if k % 2:
		s1 += s[int(k/2)]
	else:
		s1 = s1 + s[int(k/2-1)] + s[int(k/2)]
	return s1

print(get_middle('of'))