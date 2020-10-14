import math
def oddOrEven(arr):
	a, b = 0, 0
	for i in arr:
		if i % 2:
			a += 1
		else:
			b += 1
	if a % 2:
		return 'odd'
	else:
		return 'even'
print(oddOrEven([0, 1, 2]))
print(oddOrEven([math.sqrt(4), math.sqrt(16)]))