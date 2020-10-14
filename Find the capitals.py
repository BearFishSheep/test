def capitals(word):
	ls = []
	if word == '':
		return ls
	for i in range(len(word)):
		if 'A' <= word[i] <= 'Z':
			ls.append(i)
	return ls

print(capitals('CodEWaRs'))