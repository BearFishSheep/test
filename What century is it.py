def whatCentury(year):
	s = year[:2]
	s1 = year[2:]
	if int(s1) > 0:
		a = int(s) + 1
	else:
		a = int(s)
	s = str(a)
	if s[1] == '1' and a > 20:
		s += 'st'
	elif s[1] == '2' and a > 20:
		s += 'nd'
	elif s[1] == '3' and a > 20:
		s += 'rd'
	else:
		s += 'th'
	return s
print(whatCentury('1900'))