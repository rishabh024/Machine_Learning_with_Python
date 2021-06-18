# Developed By : Rishabh Gupta

# Question is- Write a Python program to sum all the items in a list.

from math import fsum

a = list(map(int, input("enter the space separated nos-").split()))
print(fsum(a))
