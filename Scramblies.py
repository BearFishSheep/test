def scramble(s1, s2):
	if s1 == '' and s2 == '':
		return False
	if len(s1) < len(s2):
		return False
	for i in s2:
		if i not in s1:
			return False
		if s2.count(i) > s1.count(i):
			return False
	return True
print(scramble('katas', 'steak'))
