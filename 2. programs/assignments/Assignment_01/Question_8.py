# Developed By : Rishabh Gupta

# Question is- Write a program to check Armstrong number in Python-

# Solution:-

a = eval(input("enter no-"))
no = a
b = a
sum = 0
count = 0

while(b > 0):  # to count no of digits in given no
    b = b // 10
    count += 1

while(a > 0):
    r = a % 10
    sum += (r ** count)
    a = a // 10

print(no, "is armstrong no") if (sum == no) else print(no, "is not a armstrong no")
