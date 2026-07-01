def recursive(n):
    if n==0 or n==1:
        return 1
    return n*recursive(n-1)
num=int(input())
print(recursive(num))