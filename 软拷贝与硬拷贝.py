"""#软拷贝
lt = ["hello", "world", "123"]
ls=lt
print(ls)
lt.clear()
print(ls)
"""
#硬拷贝
lt = ["hello", "world", "123"]
ls=lt.copy()
print(ls)
lt.clear
print(ls)