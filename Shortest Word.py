def find_short(s):
	ls = s.split()
	ls1 = []
	for i in ls:
		ls1.append(len(i))
	return min(ls1)

print(find_short("bitcoin take over the world maybe who knows perhaps"))