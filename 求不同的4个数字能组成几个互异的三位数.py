i,m=4,1
a=[1,2,3,4]
while i>=1:
    m*=i
    i-=1
l1=[i*100+j*10+k for i in a for j in a for k in a if i!=j and j!=k and i!=k]
print("{}个".format(m))
print(l1)