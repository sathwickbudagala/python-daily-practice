lst=list(map(int,input().split()))
target=int(input())
if target in lst:
    for i in range(len(lst)):
        if lst[i]==target:
            print(i)
else:print("target isnt there in list")