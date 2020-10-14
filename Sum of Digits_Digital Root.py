def digital_root(n):
	sum = 0
	while n:
		sum += n % 10
		n = int(n / 10)
	if sum < 10:
		return sum
	else:
		return digital_root(sum)
print(digital_root(493193))