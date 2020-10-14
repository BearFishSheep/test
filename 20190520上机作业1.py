class Shape:
	def __init__(self, name):
		self.name = name
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
class Triangle(Shape):
	def __init__(self, name, width, height, a, b):
		super().__init__(name)
		self.width = width
		self.height = height
		self.a = a
		self.b = b
	def Area(self, width, height):
		s = 0.5 * self.width * self.height
		print("{}的面积为：{}".format(self.name, s))
	def Perimeter(self, width, a, b):
		c = self.width + self.a + self.b
		print("{}的周长为：{}".format(self.name, c))
class Rectangle:
	def __init__(self, name):
		self.name = name
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
class Square(Rectangle):
	def __init__(self, name, a):
		super().__init__(name)
		self.a = a
	def Area(self, a):
		s = self.a ** 2
		print("{}的面积为：{}".format(self.a, s))
	def Perimeter(self, a):
		c = self.a * 4
		print("{}的周长为：{}".format(self.a, c))

Triangle1 = Triangle('三角形', 2, 3, 2, 2)
Triangle1.Area(2, 3)
Triangle1.Perimeter(2, 2, 2)
Square1 = Square('正方形', 2)
Square1.Area(2)
Square1.Perimeter(2)