#每一行输出列表形式
import csv
f = open("D:\\women.csv", 'r')
reader = csv.reader(f)
for i in reader:
	print(i)
"""
#每一个输出字符串形式
f = open("D:\\women.csv", 'r')
for i in f:
	print(i)
"""