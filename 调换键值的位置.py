dc = {'a': 10, 'b': 34, "c" : 56} 
#print({j:i for i,j in dc.items()})

a=zip(dc.values(), dc.keys())
print(a)