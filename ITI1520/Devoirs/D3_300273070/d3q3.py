def listFunc(l):
    index = 0
    p = 0
    while index < (len(l)):
        if l[index] > 0:
            p = p + 1
        index = index + 1
    print(p)

liste = str(input("Enter numbers separated by commas : "))
#print("Input string", liste)

lst = liste.split(",")
#print("list", lst)

l = []
for i in lst:
    l.append(int(i))

#print(l)

listFunc(l)
