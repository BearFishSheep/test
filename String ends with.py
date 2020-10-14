def solution(string, ending):
	for i in range(len(ending)):
		if string[len(string)-len(ending)+i] != ending[i]:
			return False
	return True

print(solution('abc', 'd'))