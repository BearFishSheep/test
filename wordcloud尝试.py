import wordcloud
import jieba

f = open('D://song.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()

ls = jieba.lcut(txt)
newtxt = ' '.join(ls)

cloud = wordcloud.WordCloud(font_path = 'simhei.ttf', background_color = 'white', \
	width = 800, height = 600, max_font_size = 100).generate(newtxt)
cloud.to_file('test.png')