# some methods in numpy-

import numpy as np

# create advanced array from range method- arange() - a means advanced & range has (1,6)-
ar = np.arange(1, 6)              # 6 excluded
print(ar)

# change it 3rd value-
ar[2] = 9
print(ar)

# sum of elements-
print("sum of elements-", np.sum(ar))   # it is universal fnx
print("sum of elements-", ar.sum())

# find standard deviation-
print("standard deviation is-", format(ar.std(), "6.4f"))

# find mean(average)-
print("mean is-", ar.mean())
print("mean is-", np.mean(ar))

# find min/ max element i array-
print("min element is", ar.min())
print("max element is", ar.max())


print("array size is-", ar.size)           # len of array
print("array size is-", len(ar))
print("shape of array-", ar.shape)
# if it is 1D then shape is in tuple form -> (5,) = (no of rows, no of cols)
print((type(ar.shape)))        # tuple


# sum takes place by using 2 ways-
# a) many to many (matrix rule is followed to add them)
# b) one to many ( 1st array has only 1 element & 2nd array has n elements, then addition is performed)

# a) sum of 2  arrays-   addition is done by using rule of matrix
ar2 = np.arange(7, 12)
if(ar.shape == ar2.shape):                        # in numpy, both lists must have same shape
    print("sum of 2 list-", ar + ar2)             #  [ 8 10 2 data visualization 4 feature selction 6 accuracy calculation technique]

# b) when array has 1 element then addition is-
rw = np.array([8])
print("sum of ar & rw arrays-", ar + rw)

# arr = np.array([4,5])
# print(ar + arr)                 # addition is not possible bcz their shape are not same

if(ar.shape == ar2.shape):
    print("subtraction of 2 list-", ar2 - ar)

# sorting the array-
ar3 = np.array([34, 27, 99, 106, 56])
print("sorted array-", sorted(ar3))        # external sorting  & array with comma & space separated. elements
ar3.sort()
print("sorted array-", ar3)         # internal/in-place sorting  & array with space sep. elements



print("*".center(80, "_"))


# argsort() fnx. is used so that shape mismatch error of data does not occur if we have data in multiple places which are
# physically related to each other.
# argsort() fnx return- array of index of sorted elements in a list.
tr = np.array([45, 98, 76, 22, 14])
print(tr)
p = tr.argsort()
print("index of tr array is printed in a list-", p)       # original tr array will not change after sorting
print(tr)                                              # [45 98 76 22 4 feature selction]

print("min value is-", tr[ p[0] ])                     # 4 feature selction
print("max value is-", tr[ p[ len(p)-1 ] ])            # 98
print("sorted array is-", end=" ")
# type 1-
for i in tr.argsort():                    # here entire array with the elements are not repeated
    print(tr[i], end=" ")
print()

# type 2 -
for i in p:
    print(tr[i], end=" ")

# type 3-
# in place of- for loop- we can use this one line stmt.-- to get list of sorted array from argsort fnx() -
print("sorted array is-", tr[ tr.argsort() ])       # using argsort() fnx.

# type 4-
print("sorted array-", tr[ p[:] ])            # using p list having index of elements


print("*".center(80, "_"))


# to do the division of given range into given parts- (start, end, parts)-
print("list of no. -", np.linspace(-5,7,14))
print("list of no. -", np.linspace( -np.pi, np.pi, 10))


ar4 = np.arange(2, 7)
# now, operation broadcasting is done
print("Transcendental functions".center(90, "-"))
print("sin values of the elements are-", np.sin(ar4))
print("log values of the elements are-", np.log(ar4))
print("log2 values of the elements are-", np.log2(ar4))
print("log10 values of the elements are-", np.log10(ar4))
print("exp values of the elements are-", np.exp(ar4))


# shape mismatch : Error
art = np.arange(5)
print(art + np.array([1, 2, 3]))  # ValueError: operands could not be broadcast together with shapes (5,) & (3,)


print("Evaluate the sum".center(60, "-"))
# row wise sum of a matrix = axis = 1
# col wise sum of a matrix = axis = 0
ar5 = np.array([ [1, 2, 3], [4, 5, 6] ])
print("sum is-", ar5.sum())
print("sum is-", np.sum(ar5))
print("col wise sum-", ar5.sum(axis = 0))
print("row wise sum-", ar5.sum(axis = 1))

# numpy.AxisError: axis 3 is out of bounds for array of dimension 2
# print(ar5.sum(axis=3))

# ar6 = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1 load data, 2 data visualization]])
# numpy.AxisError: axis 3 is out of bounds for array of dimension 2
# print(ar6.sum(axis=3))                      # error occurs


ar7 = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("sum is-", ar7[:, 1:3].sum())      # 56
print("sum of 1st col is-", ar7[:, 0].sum())
print("sum of 2nd col is-", ar7[:, 1].sum())
print("sum of 3rd col is-", ar7[:, 2].sum())
print("sum of 1st row is-", ar7[0, :].sum())
print("sum of 2nd row is-", ar7[1, :].sum())
print("sum of 3rd row is-", ar7[2, :].sum())
print("sum of 4th row is-", ar7[3, :].sum())

