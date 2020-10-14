def mxdiflg(a1, a2):
	if a1 == [] or a2 == []:
		return -1
	else:
		ls1 = []
		ls2 = []
		for i in a1:
			ls1.append(len(i))
		for j in a2:
			ls2.append(len(j))
		x1, x2 = max(ls1), min(ls1)
		y1, y2 = max(ls2), min(ls2)
		return max(abs(x1-y2), abs(x2-y1))		
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(a1, a2))