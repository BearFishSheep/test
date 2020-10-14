def friend(x):
	ls = []
	if len(x) == 0:
		return ls
	for i in x:
		if len(i) == 4:
			ls.append(i)
	return ls

print(friend(["Ryan", "Kieran", "Mark",]))