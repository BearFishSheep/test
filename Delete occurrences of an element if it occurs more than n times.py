def delete_nth(order,max_e):
	new_order=[]
	idx_order={x:0 for x in order}
	for item in order:
		if idx_order[item]<max_e:
			idx_order[item]+=1
			new_order.append(item)
	return new_order

order=[1,1,2,2,2,3,3,3,3,4]
print(delete_nth(order,2))