def is_triangle(a, b, c):
	if a>b:
		a,b=b,a
	if a>c:
		a,c=c,a
	if b>c:
		b,c=c,b
	if a+b>c:
		return True
	else:
		return False

a=eval(input())
b=eval(input())
c=eval(input())
if is_triangle(a,b,c):
	print("yes")
else:
	print("no")