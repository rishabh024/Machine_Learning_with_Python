# it is advanced method to load data by using numpy

import numpy as np
filename = 'indians-diabetes.data.csv'
raw_data = open(filename, 'r')

#data variable has advanced level of array by using numpy
# to read data
data = np.loadtxt(raw_data, delimiter=",")

# here we get o/p as tuple - (rows ,cols)
print('\n\n', data.shape)

# close the pointer to make memomry space free-
raw_data.close()

print('\n data is-\n', data)

for i in data:
    print(i)
