def disemvowel(string):
	for i in string:
		if i=='a' or i=='A':
			string=string.replace(i,'')
		elif i=='e' or i=='E':
			string=string.replace(i,'')
		elif i=='o' or i=='O':
			string=string.replace(i,'')
		elif i=='i' or i=='I':
			string=string.replace(i,'')
		elif i=='u' or i=='U':
			string=string.replace(i,'')
	return string

s=input()
print(disemvowel(s))
		