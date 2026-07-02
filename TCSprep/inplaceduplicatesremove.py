lst=list(map(int,input().split()))
left=0
for i in range(1,len(lst)):
    if lst[i]!=lst[left]:
        left+=1
        lst[left]=lst[i]
print(lst)

'''
Given a sorted array, remove duplicates in-place
 so each element appears only once, and return
   the count of unique elements.
   '''