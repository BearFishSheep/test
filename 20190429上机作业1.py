import csv
ls = []
with open ('D:\\IRIS.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for data in reader:
		for item in data:
			if item.isdigit():
				ls.append(int(item))
	print(ls)