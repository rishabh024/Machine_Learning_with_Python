# Developed By : Rishabh Gupta

# Question is- Write a Python program to shuffle and print a specified list.

import random

a = list(map(int, input("enter space separated nos-").split()))
random.shuffle(a)
print("after shuffling, list will be-", a)
