class Shape:
	def __init__(self, a, b, name = ''):
		self.a = a
		self.b = b
		self.name = name
	def setname(self, name):
		self.name = name
	def getname(self):
		return self.name
	def getarea(self):
		pass
class Triangle(Shape):
	def __init__(self, a, b, name = ''):
		super().__init__(a, b, name = '')
	def getarea(self):
		print("{}的面积为{}".format(self.getname(), 0.5 * self.a * self.b))
class Rectangle(Shape):
	def __init__(self, a, b, name = ''):
		super().__init__(a, b, name = '')
	def getarea(self):
		print("{}的面积为{}".format(self.getname(), self.a * self.b))
def Calculate(s):
	s.getarea()

t = Triangle(1, 2)
t.setname('三角形')
r = Rectangle(2, 3)
r.setname('矩形')
ShapeList = [t, r]
for i in ShapeList:
	Calculate(i)
print('{} and {}'.format(t.getname(), r.getname()))