datas = [
    ['姓名','张三'],['年龄','18'],['体重','65'],['身高','170']
]
with open("D:\\75.csv", "w", newline='') as f:
    for row in datas:
        f.write(",".join(row) + "\n")	#行与行之间用空格分开，行内用逗号分开