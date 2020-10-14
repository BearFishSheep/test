import jieba
f = open('D://novel.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()
words = jieba.lcut(txt)
counts = {}
for i in words:
	if len(i) == 1:
		continue
	else:
		counts[i] = counts.get(i, 0) + 1
items = list(counts.items())
items.sort(key = lambda x : x[1], reverse = True)
for i in range(5):
	word, count = items[i]
	print("{0:<10}{1:>5}".format(word, count))