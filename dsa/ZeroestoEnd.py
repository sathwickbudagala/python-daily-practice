lst = list(map(int, input().split()))

non_zero = []
zeros = []

for i in lst:
    if i == 0:
        zeros.append(i)
    else:
        non_zero.append(i)

print(non_zero + zeros)