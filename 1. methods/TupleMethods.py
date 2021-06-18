# methods in tuple

t = ('a', 'e', 'i', 'o', 'i', 'u')

# index-
print('The index of e:', t.index('e'))

# 'i' after the 4th index is searched
index = t.index('i', 4)  # 6
print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = t.index('i', 2, 5)  # Error!
print('The index of i:', index)

# count-
r = ('a', ('a', 'b'), ('a', 'b'), [3, 4])

# count element ('a', 'b')
print("count = ", r.count(('a', 'b')))
