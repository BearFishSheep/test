def create_phone_number(n):
	s = '('
	for i in range(3):
		s += str(n[i])
	s += ') '
	for i in range(3,6):
		s += str(n[i])
	s += '-'
	for i in range(6,10):
		s += str(n[i])
	return s

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(a))