def sequence_sum(begin_number, end_number, step):
	if begin_number > end_number:
		return 0
	i = begin_number
	sum = 0
	while i <= end_number:
		sum += i
		i += step
	return sum
print(sequence_sum(2, 6, 2))