lst=list(map(int,input().split()))
for i in range(1,max(lst)+1):
    if i not in lst:
        print(i,end=" ")