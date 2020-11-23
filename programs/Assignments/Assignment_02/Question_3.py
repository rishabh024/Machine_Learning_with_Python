# Developed By : Rishabh Gupta

# Question is-  Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

a = list(input("enter the list of strings-").split())
count = 0

for i in a:
    if ( (len(i) >= 2) and (i[0] == i[-1]) ):
       count = count + 1

print("No of strings (whose length is 2 or more and "
      "the first and last character of the string are same) in a given list are-", count)
