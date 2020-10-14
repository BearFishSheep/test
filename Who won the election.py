def getWinner(listOfBallots):
	ls = list(listOfBallots)
	s = set(ls)
	for i in s:
		if ls.count(i) > len(ls)/2:
			return i
	return None
print(getWinner(("A", "A", "A", "B", "B", "B")))