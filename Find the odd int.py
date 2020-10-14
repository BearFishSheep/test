def find_it(seq):
	s = set(seq)
	for i in s:
		if seq.count(i) % 2:
			return i

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(seq))