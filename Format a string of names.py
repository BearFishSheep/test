def namelist(names):
	s = ''
	if len(names) == 0:
		return s
	elif len(names) == 1:
		s += names[0]['name']
	elif len(names) == 2:
		s = s + names[0]['name'] + ' & ' + names[1]['name']
	else:
		k = len(names)
		for i in range(k-2):
			s = s + names[i]['name'] + ', '
		s = s + names[k-2]['name'] + ' & '+ names[k-1]['name']
	return s
#print(namelist([ {'name': 'Bart'}]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))