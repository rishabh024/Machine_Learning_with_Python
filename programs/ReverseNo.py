# find reverse & check if it is palindrome or not

a = int(input("enter no"))
no = a
sum = 0

while (a > 0):
    r = a % 10
    sum = (sum * 10) + r
    a = a // 10

print("reverse no is=", sum, end=' ')
if (sum == no):
    print(" and this no is palindrome")
else:
    print("and this no is not palindrome")