def increment_string(strng):
	if len(strng) == 0:
		strng += '1'
	else:
		if '0' <= strng[len(strng)-1] <= '8':
			a = ord(strng[len(strng)-1]) - ord('0')
			strng[len(strng)-1] = strng[len(strng)-1].replace('a', 'a+1')
		elif strng[len(strng)-1] == '9':
			strng[len(strng)-1] = strng[len(strng)-1].replace('9', '1')
			strng += '0'
		else:
			strng += '1'
	return strng

print(increment_string('foobar099'))