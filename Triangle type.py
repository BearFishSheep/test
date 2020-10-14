def triangle_type(a, b, c):
	ls = [a, b, c]
	ls = sorted(ls)
	if ls[0] + ls[1] <= ls[2]:
		return 0
	elif ls[0]**2 + ls[1]**2 == ls[2]**2:
		return 2
	else:
		a = (ls[0]**2+ls[1]**2-ls[2]**2)/(2*ls[0]*ls[1])
		if a > 0:
			return 1
		else:
			return 3
print(triangle_type(7, 12, 8))