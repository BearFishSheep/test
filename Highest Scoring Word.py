def high(x):
	ls1 = x.split()
	ls2 = []
	for i in ls1:
		sum1 = 0
		for k in i:
			sum1 = sum1 + ord(k) - ord('a') + 1
		ls2.append(sum1)
	index = 0
	for i in range(1, len(ls2)):
		if ls2[i] > ls2[index]:
			index = i
	return ls1[index]
print(high('man i need a taxi up to ubud'))