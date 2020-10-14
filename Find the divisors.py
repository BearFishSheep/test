def divisors(n):
	ls=[]
	s="A is prime"
	if n==2:
		s="2 is prime"
		return s
	else:
		for i in range(2,n):
			if n%i == 0:
				ls.append(i)
		if len(ls)==0:
			s=s.replace('A',str(n))#将数字转换为字符串，用str函数
			return s
		else:
			return ls

n=eval(input("请输入一个大于1的数："))
print(divisors(n))