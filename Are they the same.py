def comp(a, b):
	if a == [] and b == []:
		return True
	elif a == [] or b == []:
		return False
	a = sorted(a)
	b = sorted(b)
	c = []
	for i in a:
		c.append(i*i)
	if c == b:
		return True
	else:
		return False
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a, b))