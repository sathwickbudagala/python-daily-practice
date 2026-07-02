lst=list(map(int,input().split()))
final=[]
for i in range(len(lst)-1,-1,-1):
    final.append(lst[i])
print(final)