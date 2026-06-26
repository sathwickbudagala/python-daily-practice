sen=str(input())
for i in range(len(sen)):
    if i==0:
        print(sen[i].upper(),end="")
    else:
        if sen[i-1]==" ":
            print(sen[i].upper(),end="")
        else:
            print(sen[i],end="")