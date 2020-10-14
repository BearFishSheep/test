keywords = ['and','def','elif','else','for','if','in']
with open("D:\\aaa.ipynb", "r") as f:
    f1 = f.readlines()
    print(f1)
    ls = []
    for i in f1:
        i = i.split()
        ls.append(i)
    fo = open("D:\\aaa.ipynb", "w+")
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            x = ls[i][j]
            if x not in keywords:
                x = x.upper()
            if j == len(ls[i])-1:
                fo.write(x + "\n")
            else:
                fo.write(x + "\n")
    fo.close()