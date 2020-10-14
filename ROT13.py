def rot13(message):
	ls = list(message)
	ls1 = [] 
	#chr函数返回编码对应的字符
	#ord函数返回字符对应的编码
	#想要操作字符串里的字母让他们后移可以采用chr,ord函数
	for i in ls:
		if 'a' <= i <='m' or 'A' <= i <='M':
			ls1.append(chr(ord(i) + 13)) 
		elif 'n' <= i <='z' or 'N' <= i <='Z':
			ls1.append(chr(ord(i) - 13))
		else:
			ls1.append(i)
	message = ''.join(ls1)
	return message

print(rot13('test'))