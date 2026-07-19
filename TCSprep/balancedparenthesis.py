lst = input()
final = []
count = 0
zount = 0

if len(lst) == 1:
    print("unbalanced parenthesis")

else:
    for i in lst:

        if i in "{[(":
            final.append(i)
            count += 1

        elif i in "}])":

            if not final:
                print("unbalanced parenthesis")
                zount += 1
                break

            z = final.pop()

            if (z, i) in [('(', ')'), ('[', ']'), ('{', '}')]:
                count += 1
            else:
                print("unbalanced parenthesis")
                zount += 1
                break

    if zount == 0 and count == len(lst) and not final:
        print("balanced parenthesis")