def two_oldest_ages(ages):
	ages = sorted(ages)
	return ages[-2:]

print(two_oldest_ages([6, 5, 83, 5, 3, 18]))