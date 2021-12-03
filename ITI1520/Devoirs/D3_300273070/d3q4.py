def listFunc(l):
    index1 = 0
    index2 = 1
    dup = False
    p = 0
    for i in range(1, len(l)):
        if l[index1] == l[index2]:
            dup = True
            return dup
        else:
            dup = False
            index1 += 1
            index2 += 1
    return dup
        

liste = str(input("Enter numbers separated by commas : "))
#print("Input string", liste)

lst = liste.split(",")
#print("list", lst)

l = []
for i in lst:
    l.append(int(i))

#print(l)

dup = listFunc(l)
print(dup)
