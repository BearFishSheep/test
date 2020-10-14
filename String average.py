def average_string(s):
	dc = {'zero':0 ,'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
	ls = s.split()
	str1 = ''
	sum1 = 0
	if s == '':
		return 'n/a'
	for i in ls:
		if i not in dc.keys():
			str1 = 'n/a'
			return str1
		else:
			sum1 += dc[i]
	if sum1 == 0:
		return 'zero'
	sum1 = int(sum1/len(ls))
#用二元组来实现通过值求键：
	for key, value in dc.items():
		if value == sum1:
			return key
print(average_string("four six two three"))