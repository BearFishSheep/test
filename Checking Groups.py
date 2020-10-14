def group_check(s):
	if s == '':
		return True
	ls = []
	for i in s:
		if i == '(' or i == '[' or i == '{':
			ls.append(i)
		elif i == ')':
			if len(ls) == 0:
				return False
			elif ls[len(ls)-1] != '(':
				return False
			else:
				a = ls.pop(len(ls)-1)
		elif i == ']':
			if len(ls) == 0:
				return False
			elif ls[len(ls)-1] != '[':
				return False
			else:
				a = ls.pop(len(ls)-1)
		elif i == '}':
			if len(ls) == 0:
				return False
			elif ls[len(ls)-1] != '{':
				return False
			else:
				a = ls.pop(len(ls)-1)
	if len(ls):
		return False
	return True
print(group_check('([]())'))