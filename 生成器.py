"""g=(i**2 for i in range(10))
for n in g:
	print(n)
"""

def f1():
	for i in range(10):
		yield i**2

print(list(f1()))
print(list(f1()))