lst=list(map(int,input().split()))
final={}

for i in lst:
    if i in final:
        final[i]+=1
    elif i not in final:
        final[i]=1
for i in final:
    if final[i]==1:
        print(i)
        break