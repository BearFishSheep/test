def sum_two_smallest_numbers(numbers):
	ls = []
	for i in numbers:
		if i > 0:
			ls.append(i)
	a = min(ls)
	b = ls.remove(a)
	c = min(ls)
	return (a + c)
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))