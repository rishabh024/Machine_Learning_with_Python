# Developed By : Rishabh Gupta

# Question is- Write a Python program to concatenate following dictionaries to create a new one.

a = list(map(int, input("enter keys-").split()))
b = list(map(str, input("enter values-").split()))
dict_d1 = {}
j = 0
for i in a:
    dict_d1[i] = b[j]
    j = j + 1

c = list(map(int, input("enter keys-").split()))
d = list(map(str, input("enter values-").split()))
dict_d2 = {}
k = 0
for i in c:
    dict_d2[i] = d[k]
    k = k + 1


# to concatenate the following dictionaries--
dict_new = {}
for i in dict_d1:
    dict_new[i] = dict_d1[i]
for j in dict_d2:
    dict_new[j] = dict_d2[j]

print("\nnew dictionary is-", dict_new)
