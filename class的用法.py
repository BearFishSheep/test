class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def setname(self, name):
		self.name = name
	def getname(self):
		return self.name
	def setage(self, age):
		self.age = age
	def getage(self):
		return self.age
class Student(Person):
	def __init__(self, name, age, id):
		super().__init__(name, age)
		self.id = id
	def getid(self):
		return self.id
	def setid(self, id):
		self.id = id

a = Student('zhangsan', 18, '10001')
#a.setname('zhangsan')
#a.setage(18)
#a.setid('10001')
print("姓名：{}，年龄：{}，学号：{}".format(a.getname(), a.getage(), a.getid()))