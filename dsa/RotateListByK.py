lst=list(map(int,input().split()))
target=int(input())
if target>len(lst):
    target=target%len(lst)
lst2=[]
for i in range(target,0,-1):
    lst2.append(lst[-i])
lst1=[]
n=len(lst)-target
for i in range(n):
    lst1.append(lst[i])
print(lst2+lst1)