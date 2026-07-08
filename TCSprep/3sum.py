arr=list(map(int,input().split()))
final=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[k]==0:
                final.append([arr[i],arr[j],arr[k]])
print(final)
'''

three sum equals 0
'''