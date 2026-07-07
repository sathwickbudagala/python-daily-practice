lst=list(map(int,input().split()))
min=lst[0]
max=0
for i in lst:
    if i<min:
        min=i
    elif i-min>max:
        max=i-min
print(f"{min} and {max}")

'''
best time to buy and sell products
'''