lst=list(map(int,input().split()))
count=0
for i in range(1,len(lst)-1):
    if lst[i]<lst[i-1] and lst[i]<lst[i+1]:
        count+=(min(lst[i-1],lst[i+1])-lst[i])
print(count)