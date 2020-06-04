# list methods-

l = [1, 6, 'e', 8, 'e', 'g', 9, 8, 4, 't']

# index
print(l.index('e'))
print(l.index('e', 1, 7))
print(l.index('e', 4, 8))

# append
l.append((1, 2, 3, 4))
l.append([1, 2, 3])
l.append(1)
l.append("1")
print(l)

# extend
ls1 = ['French', 'English']
ls2 = (1, 2)
ls3 = {"rerw", 6.2, 9}
ls1.extend(ls2)
print(ls1)
ls1.extend(ls3)
print(ls1)

# other way of extend:--
# 1) by + operator:-
a = [1, 2]
b = [5, 9]
print(a + b)

# 2) by slicing of list:-
c = [99, 32]
d = [4, 7]
c[len(c):] = d
print(c)

# 3) advantage to add elements in middle of list:--
ls = [1, 2, 3, 4, 5, 6, 7, 8]
ls[2:6] = ['w', 'r', 'y', 'f']
print(ls)

# insert
mixed_list = [{1, 2}, [5, 6, 7]]
t = (3, 4)
mixed_list.insert(1, t)
print(mixed_list)

# remove
animals = ['cat', 'dog', 'dog', "rat", 'dog']
animals.remove('dog')
print(animals)

# pop
animals.pop()  # last elem. removed
animals.pop(-1)
print(animals)

# also use del to remove elem.:-
del animals[-3]
print(animals)

# count
m = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
print(m.count([3, 4]))

# reverse
m.reverse()
print(m)

# other way to get reverse element individually, inside the loop only:-
for i in reversed(m):
    print(i)

# sort
lt = [2, 6, 4, 9]
# lt.sort(reverse=True)
sorted(lt, reverse=False)
print(lt)

# copy
l1 = [1, 2, 3]
l2 = l1.copy()
print(l2)

# clear
l1.clear()
print(l1)
