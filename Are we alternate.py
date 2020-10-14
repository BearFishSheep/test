def is_alt(s):
	l = list(s)
	l1 = ['a', 'e', 'i', 'o', 'u']
	if len(l) % 2 == 0:
		i = 2
		if l[0] in l1 and l[1] not in l1:
			while i < len(l) - 1:
				if l[i] in l1 and l[i+1] not in l1:
					i += 2
				else:
					return False
		elif l[0] not in l1 and l[1] in l1:
			while i < len(l) - 1:
				if l[i+1] in l1 and l[i] not in l1:
					i += 2
				else:
					return False
		else:
			return False
	else:
		i = 2
		if l[0] in l1 and l[1] not in l1:
			while i < len(l) - 1:
				if l[i] in l1 and l[i+1] not in l1:
					i += 2
				else:
					return False
			else:
				if l[i] not in l1:
					return False
		elif l[0] not in l1 and l[1] in l1:
			while i < len(l) - 1:
				if l[i+1] in l1 and l[i] not in l1:
					i += 2
				else:
					return False
			else:
				if l[i] in l1:
					return False
		else:
			return False
	return True
print(is_alt('yaya'))