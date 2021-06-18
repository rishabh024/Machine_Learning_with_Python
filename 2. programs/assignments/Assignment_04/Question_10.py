# Developed By : Rishabh Gupta

# Question is- Write a Python function to check whether a string is a pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"


a = input("enter any string--")
a = a.upper()

lst_index = list(range(0, 91))

for i in range(0, 91):
    lst_index[i] = 0

for i in a:
    if( i != " "):
        lst_index[ord(i)] = lst_index[ord(i)] + 1


if(sum(lst_index) >= 26):
     print("the given string is a pangram")
else:
     print("the given string is not pangram")
