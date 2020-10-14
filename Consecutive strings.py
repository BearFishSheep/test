def longest_consec(strarr, k):
	ls = []
	s = ''
	if len(strarr) == 0 or k > len(strarr) or k <= 0:
		return s
	for i in range(len(strarr) - k + 1):
		j, a = 0, 0
		while j < k:
			a += len(strarr[i+j])
			j += 1
		ls.append(a)
	m = max(ls)
	for i in range(len(ls)):
		if m == ls[i]:
			index = i
			break
	j = 0
	while j < k:
		s += strarr[index+j]
		j += 1
	return s
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))