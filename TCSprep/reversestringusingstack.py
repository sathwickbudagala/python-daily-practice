name=str(input())
ame=list(name)
final=[]
for i in range(len(ame)):
    final.append(ame.pop())
print("".join(final))