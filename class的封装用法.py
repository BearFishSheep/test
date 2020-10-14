class Stduent():
	def __init__(self, id, name, score = 0):
		self.id = id
		self.name =  name
	def setscore(self, score):
		self.score = score
	def getscore(self):
		return self.score
	
s1 = Stduent('10001', 'ZhangSan')
s2 = Stduent('10002', 'LiSi')
s1.setscore(65)
s2.setscore(56)
print('{}的学号为{}，成绩为{}'.format(s1.name, s1.id, s1.getscore()))
print('{}的学号为{}，成绩为{}'.format(s2.name, s2.id, s2.getscore()))