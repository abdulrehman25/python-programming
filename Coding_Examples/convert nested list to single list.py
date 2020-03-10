lists = [[1,2,3,4],[5,6,7,8,9],9,10]
single_list = []
for i in lists:
    if isinstance(i,list):
        for j in i:
            single_list.append(j)
    else:
        single_list.append(i)
print(lists)
print(single_list)