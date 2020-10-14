def ip_to_int32(ip):
	sum = 0
	s = ip.split('.')
	ls = []
	ls2 = []
	for i in s:
		ls.append(int(i))
	for i in ls:
		t = i
		ls1 = []
		while t:
			ls1.append(t%2)
			t = int(t/2)
		if len(ls1) < 8:
			for j in range(len(ls1), 9):
				ls1.append(0)
		j = 7
		while j >= 0:
			ls2.append(ls1[j])
			j -= 1
	for i in range(32):
		sum = sum + ls2[i] * (2 ** (31-i))
	return sum
print(ip_to_int32('128.114.17.104'))