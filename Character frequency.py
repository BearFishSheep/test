"""
#对元组中的第几个元素进行排序
import operator
ls.sort(key = operator.itemgetter(1))
"""
import operator
def letter_frequency(text):
	ls1 = []
	for i in text:
		if 'a' <= i <= 'z':
			ls1.append(i)
		if 'A' <= i <= 'Z':
			ls1.append(i.lower())
	ls = []
	s = set(ls1)
	for i in s:
		ls.append((i, ls1.count(i)))
	ls.sort(key = operator.itemgetter(1), reverse = True)
	for i in range(len(ls)-1):
		a, b = ls[i]
		c, d = ls[i+1]
		if b == d and c < a:
			ls[i], ls[i+1] = ls[i+1], ls[i]
	return ls
print(letter_frequency('kkk . sjfdlkk jjj i h hihi'))