# Developed By : Rishabh Gupta

# Question is- Write a Python program to reverse a tuple.

a = tuple(map(int, input("enter space separated no-").split()))
print("given tuple is-", a)
new_tup = sorted(a,reverse=True)
print("reversed tuple is-", tuple(new_tup))
