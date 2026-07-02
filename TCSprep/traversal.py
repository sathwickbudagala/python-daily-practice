lst=list(map(int,input().split()))
final=[]
for i in range(len(lst)):
    final.append(f"{lst[i]}:{i}")
print(final)

'''
Given an array of integers, print each element along with its index.
'''