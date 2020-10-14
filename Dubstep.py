def song_decoder(song):
	song = song.replace('WUB', ' ')
	song = song.strip()
	ls = song.split()
	s = ''
	s = ' '.join(ls)
	return s

print(song_decoder('WUBAWUBWUBWUBBWUBCWUB'))