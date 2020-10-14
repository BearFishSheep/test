def is_isogram(s):
	s = s.lower()
	s1 = set(s)
	if len(s) == len(s1):
		return True
	else:
		return False

print(is_isogram('isogram'))