# numpy - numerical python
import numpy as np

# attributes-
# to create 1D, 2D, 3D or (n-dim.) array , use np.array() -
# in numpy, list supports operation broadcasting
ar = np.array([1, 2, 3])      # in this case- [1,2,3] is a list, but not [no. of rows, no. of cols].
print("print array", ar)

print("multiply each element of array by 5", ar * 5)
print("add 4 to each element", ar + 4)
print("print cube of each element", ar ** 3)

print("_________________________________________________")

ar1 = np.array([[1, 2, 3], [4, 5, 6]])

print("type of array is-", type(ar1))
# python automatically handles the datatype of variable- (int 32/ int 64)
print("datatype of elements is-", ar1.dtype)
print("datatype of elements is-", ar1.dtype.name)
print(ar1.itemsize)


# shape tells about the dimensions of an array in the form of (rows, column.) - (1D/2D/3D)
print("dim. of an array-", ar1.shape)

# size gives total size of array - (rows*colm.)
print("total six=ze of an array-", ar1.size)

print("_________________________________________________")

# to tell the dim. of array-
print("dim. of an array is-", ar1.ndim)

print(np.array([[1, 2], [3, 4], [5, 6]]))
print(np.array([[1, 2], [5, 6]], ndmin=2 ))
print(np.array([1, 4, 6], dtype=complex ))



# len method tells about the no. of lists exists in the outer bracket of list ie- [[1, 2, 3], [4, 5, 6]]
print("length is-", len(ar1))          # O/P - 2

# to print element at index [0,1] of array -> [row id, col id]
print(ar1[0, 1])
print(ar1[1, 2])

print("_____________________________________________________________________")

ar2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# in this type of array - ( ar[1][2] = ar[1,2] )
# in a matrix - (row & col index starts from o)
# slicing is used to get rows & columns - [row:row , col:col]
# to print matrix / to print all rows & cols of array
print(ar2[:, :])
print()
print(ar2[:2, 1:3])
print()
print(ar2[:1, 2])
print()
print(ar2[1, :])
print()
print(ar2[1, 1])
print()

# for all rows, print 1st col-
print(ar2[:, 1])
print()
# print 2th element of array-
print(ar2[2])
print()
# print even alternative rows by using slicing-
print(ar2[::2])
print()
# # print odd alternative rows
print(ar2[1::2])
print()
# # here 3rd arguments is used as step argument
print(ar2[1::1])
print()
print(ar2[1: :2, 1])



# fill all values of array by 0-
# in this case- [3,4] = [no. of rows, no. of cols] but not list.
ar3 = np.zeros([3, 4])
print(ar3)
print()
# fill all values by 1-
ar4 = np.ones([4, 3])
print(ar4)
# Note - these 0s & 1s are floating values.


# fill each value of array by 7-
ar5 = np.ones([4, 4]) * 7        # operation broadcasting
print(ar5)
print()
ar6 = np.zeros([4, 4]) + 7
print(ar6)
print()


# to create 1D array, give one argument to np.ones()-
print(np.zeros(5))
print(np.ones(4) * 12)


# Imp. Note:-
# 1) np.random.rand - It is used for uniform distribution, in the half-open interval [ 0.0, 1.0 )
# 2) np.random.randn - It is used for standard normal distribution ( mean 0 & variance 1 )


