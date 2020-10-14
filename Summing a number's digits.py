def sumDigits(number):
	number = abs(number)
	sum = 0
	while number:
		sum += number % 10
		number = int(number / 10)
	return sum
print(sumDigits(-32))