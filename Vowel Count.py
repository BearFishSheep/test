def getCount(inputStr):
	num = 0
	ls = ['a', 'e', 'i', 'o', 'u']
	for i in inputStr:
		if i in ls:
			num += 1
	return num

print(getCount('abracadabra'))