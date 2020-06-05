# set methods-

s = set()

# add-
s.add(1)
s.add(2)

tup = (1, 2)
s.add(tup)
print(s)

# update-
s.update([1, 2, 3])
print(s)
s.update((22, 75, 34, 44))
print(s)
s.update({66.45, 55.96, 101.444})
print(s)
s.update("don", "rms", "qwerty")
print(s)

# remove() / discard()-
# s.remove("don")   # error occured
s.remove("r")
print(s)
s.discard("d")
print(s)

# pop-  to remove arbitrary elememt from set-
s.pop()
print(s)

# copy-
s1 = s.copy()
print(s1)

# isdisjoint-
s2 = {2, 3, 66.45}
s3 = s.difference(s2)
print(s.isdisjoint(s3))

# clear-
s.clear()
print(s)
