# check given no is prime or not
import sys

a = eval(input("enter no-"))

if (a == 2):
    print("2 is even prime no")
    sys.exit(0)

f = 0
for i in range(2, int((a ** 0.5) + 1)):
    if (a % i == 0):
        f = 1
        break

print(a, "is prime no") if (f == 0) else print(a, "is not prime no")
