def spin_words(sentence):
	ls1 = sentence.split()
	ls2 = []
	for i in ls1:
		if len(i) >= 5:
			s = ''
			k = len(i) - 1
			while k >= 0:
				s += i[k]
				k -= 1
			ls2.append(s)
		else:
			ls2.append(i)
	s1 = ' '.join(ls2)
	return s1
print(spin_words("This is another test"))