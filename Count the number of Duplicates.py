def duplicate_count(text):
	x = 0
	ls = []
	text = text.lower()
	for i in text:
		ls.append(i)
	s = set(ls)
	for i in s:
		if ls.count(i) > 1:
			x += 1
	return x

print(duplicate_count('abcdeaBC'))