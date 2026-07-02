lst=list(map(int,input().split()))
left=0
for i in range(len(lst)):
    if lst[i]!=0:
        lst[left],lst[i]=lst[i],lst[left]
        left+=1
print(lst)


'''
iven an array, move all zeros to the end while 
keeping the relative order of
 non-zero elements — do this in-place (no extra array)
'''