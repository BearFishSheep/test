def reverse_words(text):
	ls = text.split()
	ls1 = []
	for i in ls:
		j = i[::-1]		#字符串翻转（用切片）
		ls1.append(j)
	a = ' '.join(ls1)
	return a
print(reverse_words('sihT si na !elpmaxe'))
