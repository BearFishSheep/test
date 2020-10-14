import math
def find_next_square(sq):
	if math.sqrt(sq)!=int(math.sqrt(sq)):
		return -1
	else:
		return int((math.sqrt(sq)+1)**2)

n=eval(input())
print(find_next_square(n))