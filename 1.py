import jieba

s = 'Python是最有意思的编程语言'
ls = list(jieba.cut(s))
print(ls)
