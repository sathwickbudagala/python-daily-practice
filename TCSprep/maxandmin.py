lst=list(map(int,input().split()))
max=lst[0]
for i in range(len(lst)):
    if lst[i]>max:
        max=lst[i]
print(f"max is {max}")
min=lst[0]
for i in range(len(lst)):
    if lst[i]<min:
        min=lst[i]
print(min)

'''
Given an array, find the maximum and minimum values without using built-in max()/min().
'''