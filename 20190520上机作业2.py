class A:
	def a1():
		pass
	def a2():
		pass
class B(A):
	def b1():
		super().a1()
		super().a2()
class C(B):
	def c1():