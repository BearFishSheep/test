import csv
"""
list1 = [1, 3 ,5, 7, 9, 'hello']
with open ('D:\\example1.csv', 'w') as fout:
	writer = csv.writer(fout)
	writer.writerow(list1)
"""
with open ('D:\\women.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for data in reader:
		print(data)