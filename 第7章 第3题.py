import random
def save_txt():
	f = open("D:\\73.txt", 'w')
	for row in range(10):
		a = ''
		for col in range(10):
			b = str(random.randint(1,1000))
			a = a + b + ' '
		f.write(a + "\n")
	f.close()
def save_csv():
	f1 = open("D:\\73.txt", "r")
	f2 = open("D:\\731.csv", "w")
	for i in f1:
		a=i.replace(" ", ",")
		f2.write(a)
	f1.close()
	f2.close()
	
save_txt()
save_csv()
