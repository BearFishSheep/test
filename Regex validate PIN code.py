def validate_pin(pin):
	if len(pin) != 4 and len(pin) != 6:
		return False
	for i in pin:
		if '0' <= i <= '9':
			continue
		else:
			return False
	return True
print(validate_pin('a345'))