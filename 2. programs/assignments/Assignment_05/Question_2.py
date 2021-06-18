# Developed By : Rishabh Gupta

# Question is- Write a Python program to print all permutations of a given string (including duplicates).

from itertools import permutations

lst = list("".join(m) for m in permutations(input("enter any string to print all its permutations- ")))
for i in lst:
    print(i)
