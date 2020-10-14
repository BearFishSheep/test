"""
def binary_to_string(binary):
	if binary == '':
		return ''
	ls1 = []
	s = ''
	for i in binary:
		ls = []
		t = ord(i)
		while t:
			ls.append(t%2)
			t = int(t/2)
		while len(ls) < 8:
			ls.append(0)
		j = len(ls) - 1
		while j >= 0:
			ls1.append(str(ls[j]))
			j -= 1
	s = ''.join(ls1)
	return s
print(binary_to_string('1011'))
"""
def binary_to_string(binary):
	if binary == '':
		return ''
	ls = list(binary)
	s = ''
	t = int(len(ls) / 8)
	while t:
		x = 0
		ls1 = []
		for i in range(8):
			a = ls.pop(0)
			ls1.append(a)
		for j in range(8):
			x += int(ls1[j])*(2**(7-j))
		s += chr(x)
		t -= 1
	return s
print(binary_to_string('0100100001100101011011000110110001101111'))