def duplicate_encode(word):
	word = word.lower()
	s = ''
	ls = list(word)
	for i in ls:
		if ls.count(i) > 1:
			s += ')'
		else:
			s += '('
	return s
print(duplicate_encode('(( @'))