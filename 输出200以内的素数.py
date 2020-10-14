def isprime(n):
	for j in range(2,i):
		if i%j==0:
			return 0
	return 1
print("2",end=" ")
for i in range(3,200):
	if isprime(i):
		print(i,end=" ")