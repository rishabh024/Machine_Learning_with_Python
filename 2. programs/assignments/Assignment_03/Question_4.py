# Developed By : Rishabh Gupta

# Question is- : Write a Python program to get the maximum and minimum value in a dictionary.

a = list(map(str, input("enter keys-").split()))
b = list(map(int, input("enter values-").split()))

dt = {}
k = 0
for i in a:
    dt[i] = b[k]
    k += 1

min_val = min(dt.values())
max_value = max(dt.values())

print("min value is- ", min_val)
print("max value is-", max_value)
