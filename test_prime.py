def isprime(n):
	try:
		for i in range(2, n):
			if(n % i == 0):
				return False
		else:
			return True
	except:
		return False
print(isprime(19))