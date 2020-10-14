def iq_test(numbers):
	a = numbers.split()
	b = []
	for i in a:
		if int(i) % 2:
			b.append(1)
		else:
			b.append(0)
	for i in range(len(b)):
		if b.count(b[i]) == 1:
			return i+1
print(iq_test("2 4 7 8 10"))