def rgb(r,g,b):
	t=""
	for item in [r,g,b]:
		if item < 0:
			item = 0
		elif item > 255:
			item = 255
		#zfill函数返回指定长度的字符串，不够位数前面补0
		t += str(hex(item)).replace('0x','').upper().zfill(2)
	return t

print(rgb(148,0,211))