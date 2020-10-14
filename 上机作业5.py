import random
def equals(a, b):
	for i in a:
		for j in b:
			if i== j:
				return 1
	else:
		return 0
ls1= list()
ls2= list()
for i in range(10):
	ls1.append(random.randint(1,100))
	ls2.append(random.randint(1,100))
print(ls1)
print(ls2)
if equals(ls1, ls2):
	print("两个列表中包含相同元素")
else:
	print("两个列表中不包含相同元素")
