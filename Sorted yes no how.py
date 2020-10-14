def is_sorted_and_how(arr):
	ls = sorted(arr)
	ls1 = sorted(arr, reverse = True)
	if arr == ls:
		return 'yes, ascending'
	elif arr == ls1:
		return 'yes, descending'
	else:
		return 'no'
print(is_sorted_and_how([2, 1]))


def vowel_indices(word):
	ls = []
	word = word.lower()
	for i in range(len(word)):
		if word[i] == 'a' or word[i] == 'e' or word[i] == 'o' or word[i] == 'u' or word[i] == 'i' or word[i] == 'y':
			ls.append(i+1)
	return ls
print(vowel_indices('IMapli'))