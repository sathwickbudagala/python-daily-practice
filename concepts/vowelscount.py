name=str(input())
count=0
for i in name:
    if i in 'aeiouAEIOU':
        count+=1
print(f"no of vowels are {count}")