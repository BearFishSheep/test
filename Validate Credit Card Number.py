def validate(n):
	ls1 = list(str(n))
	ls = [] 
	for i in ls1:
		ls.append(int(i))
	if len(ls) % 2:
		for i in range(len(ls)):
			if i%2:
				ls[i] *= 2
	else:
		for i in range(len(ls)):
			if i%2 == 0:
				ls[i] *= 2
	for i in range(len(ls)):
		if ls[i] > 9:
			ls[i] -= 9
	t = sum(ls)
	if t % 10 != 0:
		return False
	return True
print(validate(1230))