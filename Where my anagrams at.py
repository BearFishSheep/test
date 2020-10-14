def anagrams(word, words):
	ls = []
	for i in words:
		if len(i) != len(word):
			continue
		else:
			for j in word:
				if word.count(j) != i.count(j):
					break
			else:
				ls.append(i)
	return ls
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))