# Developed By : Rishabh Gupta

# Question is-  Write a Python function to multiply all the numbers in a list.

# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

a = list(map(int, input("enter space separated nos-").split()))
m = 1
for i in a:
    m *= i
print("multiplication of all the numbers in a list-", m)
