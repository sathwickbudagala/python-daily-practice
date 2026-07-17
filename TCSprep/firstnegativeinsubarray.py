lst=list(map(int,input().split()))
k=int(input())
final=[]
for i in range(len(lst)-k+1):
    current=lst[i:i+k]
    count=0
    for j in current:
        
        if j<0:
            count+=1
            final.append(j)
            break
        else:continue
    if count==0:
        final.append(count)
print(final)
