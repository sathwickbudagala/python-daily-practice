fount=False
name=str(input())
for i in range(len(name)):
    for j in range(i+1,len(name)):
        if name[i]==name[j]:
            print("false")
            fount=True
    if fount:
        break
else:print("true")