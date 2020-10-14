class Shape():
	def __init__(self, name = ''):
		self.name = name
	def setname(self, name):
		self.name = name
	def getname(self):
		return self.name
class Circle(Shape):
	pi = 3.14159
	def __init__(self, name, id, raidus = 0):
		super().__init__(name)
		self.id = id
	def setradius(self, radius):
		self.radius = radius
	def getradius(self, radius):
		return self.radius
	def getarea(self):
		return self.pi*self.radius**2

c = Circle('圆形', 1)
c.setradius(2)
print('该形状是{}，代号是{}，半径为{}，面积为{}'.format(c.getname(), c.id, c.radius, c.getarea()))