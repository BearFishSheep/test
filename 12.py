"""
def regex(s):
	low, upp, num = 0, 0, 0
	if len(s) < 6:
		return False
	for i in s:
		if 'a' <= i <= 'z':
			low += 1
		elif 'A' <= i <= 'Z':
			upp += 1
		elif '0' <= i <= '9':
			num += 1
	if low == 0 or upp == 0 or num == 0:
		return False
	else:
		return True

print(regex('lCN4wmP9TWy4' ))
"""
regex = 'Td9VGf' 
low, upp, num = 0, 0, 0
if len(regex) < 6:
	print('False')
else:
	for i in regex:
		if 'a' <= i <= 'z':
			low += 1
		elif 'A' <= i <= 'Z':
			upp += 1
		elif '0' <= i <= '9':
			num += 1
		else:
			print('False')
			break
	else:
		if low == 0 or upp == 0 or num == 0:
			print('False')
		else:
			print('True')