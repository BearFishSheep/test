ls= [1, 4, 9, 16, 9, 7, 4, 9, 11]
flag, sum=1, 0
for i in ls:
	i*= flag
	sum+= i
	flag*= -1
print(sum)