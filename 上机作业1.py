L1=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
L2=["Sun", "Mon", "Tue", "Tue", "Thu", "Sat"]
L3=list()
for i in L1:
	for j in L2:
		if i == j:
			break;
	else:
		L3.append(i)
print(L3)