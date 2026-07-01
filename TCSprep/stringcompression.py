name=str(input())
comp=""
count=1
for i in range(1,len(name)):
    if name[i]==name[i-1]:
        count+=1
    else:
        comp+=name[i-1]+str(count)
        count=1
print(comp)