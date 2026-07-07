lst=list(map(int,input().split()))
current=lst[0]
best=lst[0]
for i in range(1,len(lst)):
    if lst[i]<current*lst[i]:
        current=current*lst[i]
    else:current=lst[i]
    if best<current:
        best=current
print(f"{best}")
