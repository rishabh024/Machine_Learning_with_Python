# Developed By : Rishabh Gupta

# Question is- Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys.

a = list(map(int, input("enter keys from 1 to 15-").split()))

dict_new = {}
for i in a:
    dict_new[i] = i**2

print("dictionary is-\n", dict_new)
