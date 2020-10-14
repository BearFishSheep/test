def make_readable(seconds):
	a, b, c = 0, 0, 0
	if seconds <= 59:
		a = seconds
		if a < 10:
			s = '00:00:0'
			s += str(a)
		else:
			s = '00:00:'
			s += str(a)
	elif 60 <= seconds <= 3599:
		s1 = '00:'
		b = int(seconds / 60)
		seconds -= b*60
		a = seconds
		if b < 10:
			s2 = '0'
			s2 = s2 + str(b) + ':'
		else:
			s2 = ''
			s2 = s2 + str(b) +':'
		if a < 10:
			s3 = '0'
			s3 = s3 + str(a)
		else:
			s3 = ''
			s3 = s3 + str(a)
		s = s1 + s2 + s3
	else:
		c = int(seconds / 3600)
		seconds -= c*3600
		b = int(seconds / 60)
		seconds -= b*60
		a = seconds
		if c < 10:
			s1 = '0'
			s1 = s1 + str(c) + ':'
		else:
			s1 = ''
			s1 = s1 + str(c) + ':'
		if b < 10:
			s2 = '0'
			s2 = s2 + str(b) + ':'
		else:
			s2 = ''
			s2 = s2 + str(b) +':'
		if a < 10:
			s3 = '0'
			s3 = s3 + str(a)
		else:
			s3 = ''
			s3 = s3 + str(a)
		s = s1 + s2 + s3
	return s

print(make_readable(3662))