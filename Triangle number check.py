import math
def is_triangle_number(number):
	if type(number) != type(1):
		return False
	if int(math.sqrt(1 + 8*number))**2 == 1 + 8*number:
		return True
	return False
print(is_triangle_number(4))