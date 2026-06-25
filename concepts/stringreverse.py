name=str(input())
print(name[::-1])

name=str(input())
final=[]
for i in range(len(name)-1,-1,-1):
    final.append(name[i])
print(" ".join(final))