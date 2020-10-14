import random
ls=list()
for i in range(10):
	ls.append(random.randint(1, 100))
print(ls)
for i in range(10):
	if i% 2== 0:
		print(ls[i], end=" ")
print("\n")
for i in ls:
	if i% 2== 0:
		print(i, end=" ")
print("\n")
ls.reverse()
print(ls)
print(ls[9],ls[0])