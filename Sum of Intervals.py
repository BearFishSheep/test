def sum_of_intervals(intervals):
	ls = []
	for i in intervals:
		j, k = i
		ls.append(k-j)
	return sum(ls)
print(sum_of_intervals([(1, 5), (6, 10)]))