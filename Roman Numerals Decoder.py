def solution(s):
	sum = 0
	dc = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	if len(s) == 1:
		sum += dc[s[0]]
	if len(s) > 1:
		for i in range(0, len(s)-1):
			if dc[s[i]] >= dc[s[i+1]]:
				sum += dc[s[i]]
			else:
				sum -= dc[s[i]]
			if i == len(s)-2:
				sum += dc[s[i+1]]
	return sum

s = input("请输入一串罗马数字：")
print(solution(s))