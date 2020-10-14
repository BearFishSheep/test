import string
def toJadenCase(s):
	return string.capwords(s)
#capwords()实现首字母大写
#title()函数也可以实现首字母大写，不需要import
print(toJadenCase("How can mirrors be real if our eyes aren't real"))