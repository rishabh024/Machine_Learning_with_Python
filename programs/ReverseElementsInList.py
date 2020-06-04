# reverse the list & print it

a = [int(i) for i in input("enter list elements-").split()]
b = []

for i in range((len(a) - 1), -1, -1):
    b.append(a[i])
print(" reverse list is-", b)
