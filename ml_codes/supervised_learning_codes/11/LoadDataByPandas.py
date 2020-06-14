# to load data from the data file by using pandas

import pandas as p

filename = "indians-diabetes.data.csv"

heading_nmaes=['a','b','c','d','e','f','g''h','i']

# to read file
dataframe = p.read_csv(filename, names=heading_nmaes)


# it shows only first 5 & last 5 cols of dataframe and middle cols represented by periods
#  &  we also get list- [rows X cols] as o/p by printing dataframe.
print('\n\n', dataframe)
print('\n\n', dataframe.shape)             # in tuple form, we get shape = (rows, cols) as o/p
print('\n\n', type(dataframe))             # here we get type of report =  <class 'pandas.core.frame.DataFrame'>
print('\n\n', dataframe.dtypes)            # it tells the datatype of values stored by each column
print('\n\n', dataframe.describe())        # it tells the detailed info about dataframe
                                           #  &  we also get list- [rows X cols] as o/p by printing dataframe.
