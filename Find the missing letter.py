def find_missing_letter(s):
	for i in range(len(s)-1):
		if ord(s[i+1]) - ord(s[i]) != 1:
			a = chr(ord(s[i]) + 1)
	return a
print(find_missing_letter(['a','b','c','d','f']))