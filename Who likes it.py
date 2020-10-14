def likes(names):
	s = ''
	if len(names)==0:
		s = "no one likes this"
	elif len(names)==1:
		s = s + names[0] + " likes this"
	elif len(names)==2:
		s = s + names[0] + ' and ' + names[1] + ' like this'
	elif len(names)==3:
		s = s + names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
	else:
		k = len(names)-2
		s = s + names[0] + ', ' + names[1] + ' and ' + str(k) + ' others like this'
	return s

names=['Brian J. Mason', 'Quincy Rosenkreutz', 'Macky Stingray', 'Nene Romanova', 'Sylvie', 'Galatea', 'Priscilla S. Asagiri', 'Leon McNichol']
print(likes(names))