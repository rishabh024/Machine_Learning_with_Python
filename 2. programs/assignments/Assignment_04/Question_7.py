# Developed By : Rishabh Gupta

# Question is-  : Write a Python function that accepts a string and calculate the number of upper case
# letters and lower case letters.

# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

a = input("enter any string having upper & lower case letters-")

lower_count = 0
upper_count = 0
not_a_char = 0

for i in a:
    if i.islower():
        lower_count += 1
    elif i.isupper():
        upper_count += 1
    else:
        not_a_char += 1

print("No. of Upper case characters :", upper_count)
print("No. of Lower case Characters :", lower_count)
print("No. which is neither in lower case nor in upper case- ", not_a_char)
