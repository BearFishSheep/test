import csv
def isnumber(s):
	try:
		if eval(s) == type(1):
			return 1
		elif eval(s) == type(1.2):
			return 2
	except:
		return False
ls = []
with open ('D:\\BostonHouse.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for data in reader:
		for item in data:
			if isnumber(item) == 1:
				ls.append(int(item))
			elif isnumber(item) == 2:
				ls.append(float(item))
	print(ls)