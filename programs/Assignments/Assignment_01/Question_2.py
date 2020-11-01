# Developed By : Rishabh Gupta

# Question is- Write a program that accept a string from user and print weather is it palindrome or not.

# Solution:-

a = input("enter string-")
if a[:] == a[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")
