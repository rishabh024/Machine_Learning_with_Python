# find prime nos btw a & b-

a = int(input("enter a > 1-"))
b = int(input("enter b > 1-"))

lt = []
f = 0
for i in range(a, b + 1):
    f = 0
    for j in range(2, int((i ** 0.5) + 1)):
        if (i % j == 0):
            f = 1
            break
    if (f == 0):
        lt.append(i)

print("prime nos btw ", a, "&", b, " -", lt)
