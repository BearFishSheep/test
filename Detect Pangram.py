def is_pangram(s):
	ls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	s = s.lower()
	for i in s:
		if 'a' <= i <= 'z':
			t = ord(i)
			ls[t-97] += 1
	for i in ls:
		if i == 0:
			return False
	return True
print(is_pangram('he quick, brown fox jumps over he lazy dog!'))