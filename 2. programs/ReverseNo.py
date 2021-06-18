# find reverse & check if it is palindrome or not
# 1221 is palindrome no

a = int(input("enter no-"))
no = a
sum = 0

while (a > 0):
    r = a % 10
    sum = (sum * 10) + r
    a = a // 10

print("reverse no is=", sum, end=' ')

print(" and this no is palindrome") if (sum == no) else print("and this no is not palindrome")
