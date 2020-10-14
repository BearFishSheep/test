import os

os.rename('E:/demo.txt', 'E:/demox.txt')






'''
with open('E:/demo.txt', 'r') as f:
	# read方法
	# content = f.read(10)	# 读取指定字符数
	# print(content)

	# readlines方法
	content = f.readlines()
	i = 1
	for temp in content:
		print("{} : {}".format(i, temp))
		i += 1
'''