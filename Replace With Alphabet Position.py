def alphabet_position(text):
	text = text.lower()
	s = ''
	for i in text:
		if 'a' <= i <= 'z':
			s = s + str(ord(i) - ord('a') + 1) + ' '
	s = s.strip(' ')
	return s
print(alphabet_position("The sunset sets at twelve o' clock."))
