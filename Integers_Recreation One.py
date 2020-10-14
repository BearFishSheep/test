import math
def list_squared(m, n):
	ls = []
	for i in range(m, n+1):
		ls1 = []
		sum = 0
		for j in range(1, i+1):
			if i % j == 0:
				ls1.append(j)
		ls1 = [k*k for k in ls1]
		for k in ls1:
			sum += k
		m = math.sqrt(sum)
		if int(math.sqrt(sum)) == m:
			ls.append([i, sum])
	return ls

print(list_squared(250, 500))