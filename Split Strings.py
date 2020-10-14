def solution(s):
	ls = []
	if len(s) == 0:
		return ls
	if len(s) % 2:
		i = 0
		while i < len(s) - 1:
			s1 = ''
			s1 = s1 + s[i] + s[i+1]
			i += 2
			ls.append(s1)
		s1 = ''
		s1 = s1 + s[len(s) - 1] + '_'
		ls.append(s1)
	else:
		i = 0
		while i < len(s):
			s1 = ''
			s1 = s1 + s[i] + s[i+1]
			i += 2
			ls.append(s1)
	return ls

print(solution('abcdef'))