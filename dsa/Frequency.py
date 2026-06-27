name=str(input())
final={}
for i in name:
    if i in final:
        final[i]+=1
    elif i not in final:
        final[i]=1
print(final)
'''
Input:  [1, 2, 2, 3, 3, 3]
Output: {1: 1, 2: 2, 3: 3}
'''