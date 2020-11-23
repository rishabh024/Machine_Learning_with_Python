# Developed By : Rishabh Gupta

# Question is- Write a Python program to sort (ascending and descending) a dictionary by value.

import operator

a = list(map(str, input("enter keys-").split()))
b = list(map(int, input("enter values-").split()))

dict_d1 = {}
k = 0

for i in a:
    dict_d1[i] = b[k]
    k = k + 1

sorted_dict = sorted(dict_d1.items(), key=operator.itemgetter(1))
print("sorted dictionary is-\n", sorted_dict)
