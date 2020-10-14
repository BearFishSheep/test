def make_sentences(parts):
	s = ''
	for i in range(len(parts)-1):
		if parts[i] != ',' and parts[i] != '.' and parts[i+1] != ',' and parts[i+1] != '.':
			s = s + parts[i] + ' ' + parts[i+1]
		elif parts[i] != ',' and parts[i] != '.' and parts[i+1] == ',':
			s = s + parts[i] + parts[i+1] + ' '
	s.strip(' ')
	ls = list(s)
	if ls[len(ls)-1] != '.':
		s += '.'
	return s
print(make_sentences(['hello', 'world'])) 