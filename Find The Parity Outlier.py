def find_outlier(integers):
	ls1=[]
	ls2=[]
	for i in integers:
		if i%2 != 0:
			ls1.append(i)
		else:
			ls2.append(i)
	if len(ls1)==1:
		return ls1[0]
	else:
		return ls2[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]
))