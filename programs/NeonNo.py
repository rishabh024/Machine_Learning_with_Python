# check if it is neon no
# 9 is neon no

a = eval(input("enter no-"))
sqre = a ** 2
sum = 0

while (sqre > 0):
    r = sqre % 10
    sum = sum + r
    sqre = sqre // 10

if (sum == a):
    print(a, "is neon")
else:
    print(a, "is not neon")
