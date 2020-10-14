"""
from sympy import *
import math

x = symbols('x')
print(type(x))
# f = math.exp(x)
f = x ** 5
# A = integrate(f, (x, 1, 2))
A = integrate(f, x)
B = integrate(f, (x, 1, 2))

print(A)
print(B)
"""
#计算时尽量使用sympy带的函数公式（如sin(x),pi)，不要使用math包
from sympy import *

x = symbols('x')
f1 = 8 * x + 5
# f = integrate(f1, (x, 1, 2))
f2 = integrate(f1, x)
print( f2)
