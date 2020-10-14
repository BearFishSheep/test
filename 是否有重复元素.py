def judge(a):
	m=sorted(a)
	print(m)
	for i in range(len(m)-1):
		if m[i]==m[i+1]:
			return True
	return False

a=[1,4,2,6,3]
print(judge(a))