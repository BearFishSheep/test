def count(string):
	dc={}
	
	for i in string:
		if i in dc:
			dc[i] += 1
		else:
			dc[i] = 1

	return dc

print(count('aba'))