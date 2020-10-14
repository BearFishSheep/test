def dirReduc(arr):
	ls = []
	if len(arr) == 0:
		return ls
	for i in arr:
		if i == 'NORTH':
			if len(ls) == 0:
				ls.append(i)
			else:
				if ls[len(ls)-1] == 'SOUTH':
					a = ls.pop(len(ls)-1)
				else:
					ls.append(i)
		if i == 'SOUTH':
			if len(ls) == 0:
				ls.append(i)
			else:
				if ls[len(ls)-1] == 'NORTH':
					a = ls.pop(len(ls)-1)
				else:
					ls.append(i)
		if i == 'EAST':
			if len(ls) == 0:
				ls.append(i)
			else:
				if ls[len(ls)-1] == 'WEST':
					a = ls.pop(len(ls)-1)
				else:
					ls.append(i)
		if i == 'WEST':
			if len(ls) == 0:
				ls.append(i)
			else:
				if ls[len(ls)-1] == 'EAST':
					a = ls.pop(len(ls)-1)
				else:
					ls.append(i)
	return ls
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))