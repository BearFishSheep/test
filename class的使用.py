class Person:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def eat(self, food):
		print("Eating " + food)
	def sleep(self, hours):
		self.hours = hours
		print("Sleeping {} hours".format(hours))
	def printf(self):
		print(self.a, self.b, self.hours)

ZhangSan = Person(100, 200)
ZhangSan.eat('apple')
ZhangSan.sleep('9')
ZhangSan.printf()