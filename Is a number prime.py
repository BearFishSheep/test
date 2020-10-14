def is_prime(num):
	if num <= 0 or num == 1:
		return False
	elif num == 2:
		return True
	else:
		for i in range(2, num):
			if num % i == 0:
				return False
		else:
			return True
print(is_prime(17))