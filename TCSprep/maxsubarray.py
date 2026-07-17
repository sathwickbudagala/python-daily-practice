lst=list(map(int,input().split()))
k=int(input())
current=sum(lst[:k])
maximum=current
for i in range(k,len(lst)):
    current+=lst[i]-lst[i-k]
    maximum=max(current,maximum)
print(maximum)

'''
maximum sum sub array using sliding windows
'''