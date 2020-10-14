def valid_parentheses(s):
	ls = []
	for i in s:
		if i == '(':
			ls.append(i)
		elif i == ')':
			if len(ls) == 0:
				return False
			elif ls[len(ls)-1] == '(':
				a = ls.pop(len(ls)-1)
				continue
			else:
				return False
	if len(ls) == 0:
		return True
	else:
		return False
print(valid_parentheses("hi(hi)()"))
			