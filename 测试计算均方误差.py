import math

#Y = 2.5648 + 1.2037x
X = [1, 2, 3, 4, 5]
Y = [4, 4.5, 6, 8, 8.5]
w = [2, 1, 3, 1, 1]
e, RSS = 0, 0
for i in range(5):
	e = 2.5648 + 1.2037 * X[i] - Y[i]
	RSS += e ** 2 * w[i]

print(RSS)
print(math.sqrt(RSS/5))
#print(ESS)
"""
X = [-3, -2, -1, 0, 1, 2, 3, 4]
Y = [-3.2, -2.1, -1.2, 0.1, 0.9, 2.1, 3.3, 4]
e, s = 0, 0
for i in range(8):
	e = 1.04881 * X[i] - 0.036905 - Y[i]
	s += e**2
print(math.sqrt(s))
"""