def alphanumeric(s):
	if s == '':
		return False
	for i in s:
		if i == '_' or i == '!'\
			or i == '/' or i == '#' or i == '^':
			return False
	ls = list(s)
	if ls.count(' ') > 1:
		return False
	return True
print(alphanumeric(' a'))