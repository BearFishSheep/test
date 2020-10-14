def power_of_two(x):
	if x == 0:
		return False
	elif x == 1:
		return True
	if x % 2:
		return False
	else:
		while x != 2:
			x = int(x / 2)
			if x % 2:
				return False
		return True

print(power_of_two(512))