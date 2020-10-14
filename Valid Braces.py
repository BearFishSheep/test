def validBraces(s):
	ls = []
	for i in s:
		if i == '(' or i == '[' or i == '{':
			ls.append(i)
		elif i == ')':
			if len(ls) == 0:
				return False
			elif ls[len(ls)-1] == '(':
				a = ls.pop(len(ls)-1)
			else:
				return False
		elif i == ']':
			if len(ls) == 0:
				return False
			elif ls[len(ls)-1] == '[':
				a = ls.pop(len(ls)-1)
			else:
				return False
		elif i == '}':
			if len(ls) == 0:
				return False
			elif ls[len(ls)-1] == '{':
				a = ls.pop(len(ls)-1)
			else:
				return False
	if len(ls) == 0:
		return True
	else:
		return False
print(validBraces('(){)[]'))
