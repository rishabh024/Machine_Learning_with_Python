# find max & min no in a list

a = [int(i) for i in input().split()]

max = a[0]
min = a[0]

for i in a:
    if (max < i):
        max = i
    if (min > i):
        min = i
print("max no is", max)
print("min no is", min)
