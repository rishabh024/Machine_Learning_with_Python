# Developed By : Rishabh Gupta

# Question is- Write a Python program to get a list, sorted in increasing order by the last element
# in each tuple from a given list of non-empty tuples.

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Resulst : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


a = list(map(int, input("enter space separated no of list 1- ").split()))
b = list(map(int, input("enter space separated no of list 2- ").split()))

lst = list(zip(a, b))      # lst becomes- [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

second_element_sorted = sorted(b)

new_lst = []
for i in second_element_sorted:
    for j, k in lst:
        if( i == k):
            new_lst.append( (j, k) )

# Note - tuple() takes only 1 arg.

print(new_lst)
