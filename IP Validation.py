def is_valid_IP(strng):
	if strng == '':
		return False
	ls = strng.split('.')
	if len(ls) != 4:
		return False
	for i in ls:
#isdigit()函数用来判断字符串里的内容是否为数字
#isalpha()函数用来判断字符串里的内容是否为字母		
		if i.isdigit():
			if (int(i) < 0 or int(i) > 255) or (len(i) > 1 and i[0] == '0'):
				return False
		else:
			return False
	else:
		return True
print(is_valid_IP('123.045.067.089'))