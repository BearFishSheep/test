def format_words(words):
	ls = []
	s = ''
	if words == [] or words == None:
		return ''
	for i in words:
		if i != '':
			ls.append(i)
	if len(ls) == 0:
		return ''
	elif len(ls) == 1:
		return ls[0]
	elif len(ls) == 2:
		s = s + ls[0] + ' and ' + ls[1]
		return s
	else:
		for i in range(len(ls)-2):
			s = s + ls[i] + ', '
		s = s + ls[len(ls)-2] + ' and ' + ls[len(ls)-1]
		return s
print(format_words(['', '']))