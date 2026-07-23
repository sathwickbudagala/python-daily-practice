lst = list(map(int, input().split()))
lst.sort()
target=int(input())
lo,hi=0,len(lst)-1
while lo<=hi:
    if target==lst[(lo+hi)//2]:
        print((lo+hi)//2)
        break
    elif target<lst[(lo+hi)//2]:
        hi=(lo+hi)//2-1
    elif target>lst[(lo+hi)//2]:
        lo=((lo+hi)//2)+1