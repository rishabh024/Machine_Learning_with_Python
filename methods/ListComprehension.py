# list comprehension in python-

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[print(l[i], end=' ') for i in range(len(l))]  # print all elements
print()

l2 = [i for i in l if (i % 2 == 0)]  # print even no
print(l2)

l3 = [i for i in l if (i % 2 != 0)]  # print odd no
print(l3)

l4 = [1, 'a', 5, 8, 'f', 'k', 'y', 7, 'w', 2]
l5 = sorted([i for i in l4 if (type(i) == int)])
print("in asc. order-", l5)

l7 = sorted([i for i in l4 if (type(i) == int)], reverse=True)
print("in reverse order-", l7)

l6 = [i for i in l4 if (i not in l5)]
print("only letters-", l6)
