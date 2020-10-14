s=input("请输入一个字符串：")
s=s.lower()
count={}
for word in s:
	count[word]=count.get(word,0)+1
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
	word,count=items[i]
	print("{0:<10}{1:>5}".format(word,count))