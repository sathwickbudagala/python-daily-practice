lst=list(map(int,input().split()))
final=[]
for i in range(len(lst)):
    count=1
    for j in range(len(lst)):
        if i==j:
            continue
        else:
            count*=lst[j]
    final.append(count)
print(final)
'''
product of elements except the self
'''