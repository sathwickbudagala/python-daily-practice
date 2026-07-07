nums=list(map(int,input().split()))
final=[]
for i in range(len(nums)):
    for j in range(len(nums)-1,-1,-1):
        z=min(nums[i],nums[j])
        a=(abs(i-j))*z
        final.append(a)
print(max(final))

'''
container with most amount of water to store
'''