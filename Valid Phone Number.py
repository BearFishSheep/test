def validPhoneNumber(phoneNumber):
	if len(phoneNumber) != 14:
		return False
	digit, space, bracket, line = 0, 0, 0, 0
	for i in phoneNumber:
		if '0' <= i <= '9':
			digit += 1
		elif i == ' ':
			space += 1
		elif i == '(' or i == ')':
			bracket += 1
		elif i == '-':
			line += 1
	if digit == 10 and space == 1 and line == 1 and bracket == 2:
		return True
	return False
print(validPhoneNumber('(1111)555 2345'))