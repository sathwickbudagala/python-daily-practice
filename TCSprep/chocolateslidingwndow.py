n=int(input())
lst=list(map(int,input().split()))
k=int(input())
max=lst[0]
j=0

for i in range((len(lst)-k)+1):
    if sum(lst[j:j+k])>max:
        max=sum(lst[j:j+k])
    j+=1
print(max)