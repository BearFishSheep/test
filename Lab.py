class Solution:
	def __init__(self, x):
		self.x = x
	def reverse(self, x: int) -> int:
		flag = 0
		if self.x < 0:
			flag = 1
		rev = 0
        while x:
			rev += x % 10
			x //= 10
		
		if flag:
			rev *= -1
		return rev








'''
a = 1
b = 20
list = [1, 2, 3, 4, 5]

if  a in list:
    print("变量a在给定的列表list中")
else:
    print("变量a不在给定的列表list中")

if  b not in list:
    print("变量b不在给定的列表list中")
else:
    print("变量b在给定的列表list中")
'''

'''
fruit = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(fruit)
print("apple" in fruit)

a = set("Hello")
b = set("world")
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)
'''
'''
dict1 = {'Name': 'Lee', 'Age': 17}

print(dict1['Name'])
print(dict1['Age'])

dict1['Name'] = "Bauer"
dict1['Age'] = 30
dict1['School'] = "Python School"

print(dict1['Name'])
print(dict1['Age'])
print(dict1['School'])
'''
'''
list1 = [1, 3.14, True]
list1.append("Python")
print(list1)
print(list1.count(1))  # True也会被统计为1
list1.extend(["C++", "Java", "Go"])
print(list1)
print(list1.index(1))
print(list1)
print(list1.pop(1))
list1.remove(True)    # 删除第一个1
print(list1)
list1.reverse()
print(list1)

list1 = [1, 13, 5, 9]
list2 = list1.copy()
print(list2)
list1.clear()
print(list1)

list1 = [(2, 2), (3, 4), (4, 1), (1, 3)]

def take(elem):
    return elem[1]

list1.sort(key=take)
print(list1)
'''
'''
a = [1, 2, 3, 4, 5, 6, 7]

# 切片
print(a[::2])		# [1, 3, 5, 7]
print(a[:4])		# [1, 2, 3, 4]
print(a[::-1])		# [7, 6, 5, 4, 3, 2, 1]，列表倒置，步长为-1
'''

'''
class Employee(object):
	def __init__(self, name):
		self.name = name
	def setName(self, name):
		self.name = name
	def setSex(self, sex):
		self.sex = sex
	def setAge(self, age):
		self.age = age
	def setSalary(self, salary):
		self.salary = salary
	def show(self):
		print('name:' + self.name)
		print('sex:' + self.sex)
		print('age:' + str(self.age))
		print('salary:' + str(self.salary))

class Typer(Employee):
	def setSubsidy(self, subsidy):
		self.subsidy = subsidy
	def show(self):
		print('\n','subsidy:', self.subsidy)

emp = Employee('Mike')
emp.setName('Mike')
emp.setSex('male')
emp.setAge(20)
emp.setSalary(10000)
emp.show()

typer = Typer('Linda')
typer.setSubsidy(100)
typer.show()
print(typer)	# 内存中的地址
'''
'''
def hanoi(n, a, b, c):
	if n == 1:
		print(a + ' ---> ' + c)
	else:
		hanoi(n-1, a, c, b)		# 将a中的n-1块盘子借助c放到b上
		print(a + ' ---> ' + c)
		hanoi(n-1, b, a, c)		# 将b中的n-1块盘子借助a放到c上

hanoi(3, 'a', 'b', 'c')
'''

'''
def binSearch(a, low, high, target):
	while low <= high:
		mid =  (low + high) // 2
		
		if a[mid] == target:
			return 1
		elif a[mid] > target:
			high = mid - 1
		else:
			low = mid + 1
	return 0 

def bubbleSort(a):
	for i in range(0, len(a)-1):
		for j in range(i+1, len(a)):
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]

a = [5, 2, 9, 7, 8]
print('排序前列表：', a)
bubbleSort(a)
print('排序后列表：', a)
target = eval(input('please input an integer：'))
flag = binSearch(a, 0, len(a)-1, target)
if flag == 0:
	print('查找失败！')
else:
	print('查找成功！')
'''

'''
import re

# 用正则表达式匹配电话号码
pattern_phone = re.compile('^(\d{3})-(\d{3})-(\d{4})$')
phone = input('please input a phone number:')
phonematch = pattern_phone.match(phone)
if phonematch:
	print(phonematch.group())
else:
	print('phone number is wrong!')

'''
'''
class Networkerror(RuntimeError):
	def __init__(self, _args):
		self.args = _args

try:
	host_not_found = True
	if host_not_found:
		raise Networkerror('host not found')
except Networkerror:
	print(Networkerror.args)
'''