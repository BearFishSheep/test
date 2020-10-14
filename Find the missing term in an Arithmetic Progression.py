def find_missing(sequence):
	d = (sequence[len(sequence)-1]-sequence[0])/len(sequence)
	for i in range(len(sequence)-1):
		if (sequence[i]+d) != sequence[i+1]:
			return int(sequence[i]+d)
print(find_missing([1, 3, 5, 9]))