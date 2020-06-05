# dictionary methods

d = {'1': 'Jack', 'age': 26}

# get-
print(d.get('age'))

# update value
d['age'] = 27
print(d)

# add item
d['address'] = 'Downtown'
print(d)

# pop-
s = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
print(s.pop(4))  # Output: 16

# popitem-
print(s.popitem())

# clear-
s.clear()
print(s)

# del-
del s

# fromkeys-
a = [1, 2, 3]
ds = dict.fromkeys(a)
print(ds)  # {1: None, 2: None, 3: None}

q = 'box'
ds = dict.fromkeys(a, q)
print(ds)  # {1: 'box', 2: 'box', 3: 'box'}

keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]
vowels = dict.fromkeys(keys, value)
print(vowels)
# updating the value ie value will be - [1,2]
value.append(2)
print(vowels)

# all items-
dt = {'apple': 2, 'orange': 3, 'grapes': 4}
print(dt.items())

# all keys-
print(dt.keys())

# setdefault-
# a)-
p = {'1': 2, '3': 4}
a = p.setdefault('3')
print(a)

# b)-
p = {'1': 2}
a = p.setdefault('3')
print(a)

# c)-
p = {'1': 2}
a = p.setdefault('3', "rwq")
print(a)

# update-
d = {1: 'one', 2: 'three'}
d1 = {2: 'two'}
d.update(d1)  # updates the value of key 2
print(d)

# b)-
d1 = {3: 'three'}
d.update(d1)  # adds element with key 3
print(d)

# c)-
d = {'x': 2}
d.update(y=3, z=0)
print(d)

# values-
dt = {1: 2, 3: 4}
print(dt.values())
