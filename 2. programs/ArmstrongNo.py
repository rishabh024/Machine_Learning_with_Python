# check if given no. is armstrong no.(also called as narcissistic no/plus perfect no.)-
# 153,371,9474 are narcissistic no.
# Plus perfect no is that no if it is equal to sum of its digits raised to nth power, where n is total no of digits in a given no.

a = eval(input("enter no-"))
no = a
b = a
sum = 0
count = 0

while (b > 0):  # to count no of digits in given no
    b = b // 10
    count += 1

while (a > 0):
    r = a % 10
    sum += (r ** count)
    a = a // 10

print(no, "is armstrong no") if (sum == no) else print(no, "is not a armstrong no")
