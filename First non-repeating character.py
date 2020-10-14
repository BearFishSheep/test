def first_non_repeating_letter(string):
	s = ""
	for i in string:
		if 'a' <= i <= 'z':
			if string.count(i) + string.count(i.upper()) == 1:
				return i
		elif 'A' <= i <= 'Z':
			if string.count(i) + string.count(i.lower()) == 1:
				return i
		else:
			if string.count(i) == 1:
				return i
	return s

print(first_non_repeating_letter('W4Zv9OOngLUIh.BQvINfpmskEw'))