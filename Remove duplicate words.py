def remove_duplicate_words(s):
	ls = s.split()
	ls1 = []
	for i in ls:
		if i not in ls1:
			ls1.append(i)
	return ' '.join(ls1)
print(remove_duplicate_words('my cat is my cat fat'))