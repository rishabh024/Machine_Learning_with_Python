# check if duplicate elements exist in a list or not-

a = [int(i) for i in input("enter all values simultaneously -").split()]
dupList = []
f = 0
b = range(len(a))

for i in b:
    for j in b:
        if ((a[i] == a[j]) and (i != j)):
            dupList.append(a[i])
            break

if (len(dupList) == 0):
    print("no duplicate element exists")
else:
    print("duplicate elements-", set(dupList))
