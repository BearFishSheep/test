import math
def is_square(n):
	if n < 0:
		return False
	k = int(math.sqrt(n))
	if k**2 == n:
		return True
	else:
		return False

print(is_square(26))