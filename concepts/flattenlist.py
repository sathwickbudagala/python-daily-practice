lst=[[1, 2], [3, 4], [5, 6]]
final=[]
for i in lst:
    if isinstance(i,list):
        for j in i:
            final.append(j)
    else:
        final.append(i)