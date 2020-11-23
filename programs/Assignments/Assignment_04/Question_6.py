# Developed By : Rishabh Gupta

# Question is-  Write a Python function to check whether a number is in a given range.

a = list(map(int, input("enter 2 nos to define range--").split()))
b = eval(input("enter any no.-"))

if(b >= a[0]  and b <= a[1]):
    print("yes, entered no. is in given range")
else:
    print("no, entered no. is not in given range")
