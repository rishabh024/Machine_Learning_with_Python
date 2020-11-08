# Developed By : Rishabh Gupta

# Question is- Write a program to remove the following from:-  "www.iitkanpur.in"
# a. Remove all w’s before and after .iitkanpur.
# b. Remove all lowercase letter before and after  .iitkanpur.
# c. Remove all printable characters


# Solution- a):--
# a1 = input("enter string-")
# str1 =""
#
# for i in a1:
#     if i is "w":
#         continue
#     else:
#         str1 = str1 + i
# print(str1)




# # Solution- b):--
# a2 = input("enter string-")
# str2 =""
# lst = list(range(97, 123))
#
# for i in a2:
#     if ord(i) in lst:
#         continue
#     else:
#         str2 = str2 + i
# print("string is-", str2)




# Solution- c):--
a3 = input("enter string-")
str3 =""

for i in a3:
    if i.isprintable() == True:
        continue
    else:
        str3 = str3 + i

print(str3)


# Non- printable string--  www.ii\ttkan\bpur.i\ban
