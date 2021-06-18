# built-in methods

# abs-
print(abs(19.3554))  # 19.3554
print(abs(-23.95345))  # 23.95345
print(abs(-2 + 3j))  # 3.605551275463989 = (magnitude)

# any-
l = [0, False, 5]
print(any(l))
l1 = []
print(any(l1))
s = '000'  # '0' is True since its a string character
print(any(s))  # 0 is False
s = ''
print(any(s))  # False since empty iterable
d = {0: 'False'}  # 0 is False
print(any(d))
d = {0: 'True'}
print(any(d))  # in dictionary, keys decide true/false
d = {4: 'False'}
print(any(d))
d = {4: 'True'}
print(any(d))
d = {False: 0}  # 0 and False are false
print(any(d))
d = {'0': 'False'}  # 0 is False & '0' is True
print(any(d))
d = {0: 'False', False: 0}  # 0 and False are false
print(any(d))

# all-
d = [0]
print(all(d))  # False
d1 = [1, 'e']
print(all(d1))  # True
s = '000'
print(all(s))  # True
s = ''
print(all(s))  # True

# ascii-
text = 'Pythön is interesting'
print(ascii(text))

# bin
print(bin(345))


# convert object to binary by implementing index() method--

class Box:
    a = 1
    b = 2

    def __index__(self):
        return self.a + self.b


print('The binary equivalent of quantity is:', bin(Box()))

# bool-
print(bool(3))

# divmod-
print(divmod(2.6, 0.5))

# enumerate-
lst = ['bread', 'milk']
print(list(enumerate(lst, 10)))
lst2 = ['bread', 'milk']
print(list(enumerate(lst2)))

ls3 = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(ls3)
print(type(enumerateGrocery))
print(list(enumerateGrocery))

# by loop-
for item in enumerate(ls3):
    print(item)
print('\n')
for count, item in enumerate(ls3):
    print(count, item)
print('\n')
# changing default start value
for count, item in enumerate(ls3, 100):
    print(count, item)

# frozenset-
print(frozenset([1, 2]))


# isinstance
class Box:
    a = 5


obj = Box()
print(isinstance(obj, Box))


# issubclass-
class A:
    def __init__(AType):
        print('A is a ', AType)


class B(A):
    def __init__(self):
        A.__init__('B')


print(issubclass(B, A))

print(max('perl', 'java', 'c', 'c++', 'python', 'ruby', 'kotlin'))  # 'ruby'

a = {2: 4, -1: 0, -3: 5}
k = max(a)
print("value of max key-", a[k])


# map implementation-

def calculateSquare(n):
    return n * n


ls = (1, 2, 3, 4)
rst = map(calculateSquare, ls)
print(rst)
# converting map object to set
numbersSquare = set(rst)
print(numbersSquare)

# reversed-
# for string
seq_string = 'Python'
print(list(reversed(seq_string)))

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))

# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))

# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))

# round-
print(round(5.5))  # 6
print(round(2.665, 2))  # 2.67

# slice-
str = 'python'
ob = slice(3)
print(str[ob])  # pyt

# zip-

l1 = ['1', '2']
l2 = ['s', 'e']
print(zip(l1, l2))  # <zip object at 0x0000015EB1EBFD08>
print(tuple(zip(l1, l2)))  # (('1', 's'), ('2', 'e'))
print(list(zip(l1, l2)))  # [('1', 's'), ('2', 'e')]
print(list(zip()))  # empty iterator
print(list(zip(l1)))

# (*) operator is used with zip() to unzip the list.
lt = list(zip(l1, l2))
f, s = zip(*lt)
print("first  iterable -", f)
print("second  iterable -", s)

# labda func. & filter func.-
# Program to filter out only the even items from a list
lst = [1, 4, 4, 6, 8, 77, 34, 19]
lt = list(filter(lambda x: (x % 2 == 0), lst))
print(lt)

# Passing Multiple Iterators to map() Using Lambda
n1 = [1, 2, 3]
n2 = [4, 5, 6]
print(list(map(lambda n1, n2: (n1 + n2), n1, n2)))
