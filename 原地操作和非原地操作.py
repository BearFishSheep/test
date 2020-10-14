"""非原地操作
s1="   i love barcelona.     "
s2=s1.strip()
print(s1)
print(s2)
"""

"""非原地操作
import random
a=list()
for i in range(10):
	a.append(random.randint(1,50))
print(a)
b=sorted(a)
print(a)
print(b)
"""

#原地操作
import random
a=list()
for i in range(10):
	a.append(random.randint(1,50))
print(a)
a.sort()
print(a)