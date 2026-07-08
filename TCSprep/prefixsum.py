lst=list(map(int,input().split()))
index1=int(input())
index2=int(input())
final=[]
count=0
for i in lst:
    count+=i
    final.append(count)
print(abs(final[index2]-final[index1-1]))

'''
prefix sum
'''