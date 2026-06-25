target = int(input())
count = 0

for i in range(1, target + 1):
    if target % i == 0:
        count += 1

if count == 2:
    print("prime")
else:
    print("not prime")