def nb_year(p0, percent, aug, p):
	cnt, a = 0, p0
	while a < p:
		a = a * (1+percent/100) + aug
		cnt += 1
	return cnt

print(nb_year(1500000, 2.5, 10000, 2000000))