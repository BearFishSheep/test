def order_weight(strng):
	if strng == '':
		return ''
	ls = []
	ls2 = []
	ls3 = []
	ls4 = []
	ls5 = []
	ls1 = strng.split()
	for i in ls1:
		ls.append(int(i))
	for i in range(len(ls)):
		sum = 0
		t = ls[i]
		while t:
			sum += t % 10
			t = int(t/10)
		ls2.append(sum)
	ls2.sort()
	for j in range(len(ls)):
		sum = 0
		t = ls[j]
		while t:
			sum += t % 10
			t = int(t/10)
		ls5.append(sum)
		ls3.append(0)
	for i in range(len(ls2)):
		for j in range(len(ls5)):
			if ls5[j] == ls2[i] and ls3[j] == 0:
				ls4.append(str(ls[j]))
				ls3[j] = 1
				break
	s = ' '.join(ls4)
	return s
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))