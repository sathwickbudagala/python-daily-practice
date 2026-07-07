lst=list(map(int,input().split()))
j=0
for i in range(1,len(lst)):
    if lst[i]!=lst[j]:
        j+=1
        lst[j]=lst[i]