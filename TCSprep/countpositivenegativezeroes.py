lst=list(map(int,input().split()))
pos=0
neg=0
zer=0
for i in lst:
    if i==0:
        zer+=1
    elif i>0:
        pos+=1
    elif i<0:
        neg+=1
print(f"postives are {pos}, negatives are {neg} and zeroes are {zer}")

'''
Given an array, count how many elements are positive, negative, and zero.
'''