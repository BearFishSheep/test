"""
with open('D:\\test.txt', 'r') as f:
	s = f.readlines()
	print(s)
"""
"""
ls = ['北京', '上海', '天津', '重庆']
with open('D:\\city.csv', 'w') as f:
	f.write(','.join(ls) + '\n')
"""
"""
with open("D:\\example1.csv", 'r') as f:
	ls = []
	for line in f:
		ls.append(line.strip('\n').split(','))
	print(ls)
"""
"""
with open("D:\\example1.csv", 'r') as f:
	ls = []
	for line in f:
		ls.append(line.strip('\n').split(','))
	for row in ls:
		line = ''
		for item in row:
			line += '{:10}\t'.format(item)
		print(line)
"""
with open('D:\\song.txt', 'w+') as f:
	ls = ['唐诗', '宋词', '元曲']
	f.writelines(ls)
	f.seek(0)
	for line in f:
		print(line)