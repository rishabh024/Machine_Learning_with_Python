# Developed By : Rishabh Gupta

# Question is- Write a program to print frequency of characters in a string:-
# Sample String : ‘www.google.com'

a = input("enter any string-")
l = list(range(0, 124))

for i in range(0, 124):
    l[i] = 0

for j in a:
    l[ord(j)] = l[ord(j)] + 1

d = {}               # empty dictionary

for i in a:
    if l[ord(i)] != 0:
        d[i] = l[ord(i)]
print(d)
