def what_is_the_time(time_in_mirror):
	s = ''
	dc = {'01':'11', '02':'10', '03':'09', \
		'04':'08', '05':'07', '06':'06', \
		'08':'04', '09':'03', '10':'02', \
		'11':'01', '12':'12', '07':'05'}
	ls = time_in_mirror.split(':')
	if ls[1] == '00':
		s = s + dc[ls[0]] + ':' + '00'
	else:
		s2 = ''
		ls[1] = str(60-int(ls[1]))
		if len(ls[1]) == 1:
			s2 = s2 + '0' + ls[1]
		else:
			s2 = ls[1]
		if ls[0] == '11':
			s = s + '12' + ':' + s2
		else:
			if int(dc[ls[0]]) - 1 < 10:
				s = s + '0' + str(int(dc[ls[0]])-1) + ':' + s2
			else:
				s = s + str(int(dc[ls[0]])-1) + ':' + s2
	return s
print(what_is_the_time('11:59'))