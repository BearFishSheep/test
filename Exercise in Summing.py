def minimum_sum(values, n):
	if values == [] or n == 0:
		return 0
	if n > len(values):
		n = len(values)
	sum = 0
	values.sort()
	for i in range(n):
		sum += values[i]
	return sum
def maximum_sum(values, n):
	if values == [] or n == 0:
		return 0
	if n > len(values):
		n = len(values)
	sum = 0
	values.sort(reverse = True)
	for i in range(n):
		sum += values[i]
	return sum

a = [4, 3, 1, 5, 2]
print(minimum_sum(a, 6))
print(maximum_sum(a, 3))