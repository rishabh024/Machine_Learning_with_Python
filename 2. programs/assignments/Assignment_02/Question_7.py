# Developed By : Rishabh Gupta

# Question is- : Write a Python script to merge two Python dictionaries.

# Solution:--

# dict- 1 :-

a = list(map(int, input("enter keys-").split()))
b = list(map(str, input("enter values-").split()))
dict_d1 = {}
k = 0
for i in a:
    dict_d1[i] = b[k]
    k = k + 1
print("dictionary - 1 :-", dict_d1)


# dict- 2 :-

c = list(map(int, input("enter keys-").split()))
d = list(map(str, input("enter values-").split()))
dict_d2 = {}
m = 0
for i in c:
    dict_d2[i] = d[m]
    m = m + 1
print("dictionary - 2 :-", dict_d2)

# Now, merging the given dictionaries-
for p in dict_d2:
    dict_d1[p] = dict_d2[p]

print("on merging two dictionaries, we get-\n", dict_d1)
