"""n = eval(input('请输入一个整数：'))
print(n ** 32)
"""
"""
s = input('请输入一段文字：')
for i in s:
	print(i)
"""
"""
s = eval(input('请输入一个合法算式：'))
print(s)
"""
"""
a = eval(input('请输入一个小数：'))
print(int(a))
"""
"""
s = input('请输入一个字符串：')
ls = s.split()
for i in ls:
	print(i)
print(9 // 2)
"""
"""
def printprime(n):
	print(2, end = ' ')
	for j in range(3, n):
		for i in range(2, j):
			if j % i == 0:
				break
		else:
			print(j, end = ' ')
printprime(200)
"""
s = [1,5,2,-1,4]
s1 = sorted(s, reverse = True)
print(s1)