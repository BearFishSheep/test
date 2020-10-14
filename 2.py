import jieba
s = '今天晚上我吃了意大利面'
jieba.add_word('意大利面')
ls = list(jieba.cut(s))
print(ls)