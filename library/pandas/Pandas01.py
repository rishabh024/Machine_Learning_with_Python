# About pandas:-

import numpy as np
import pandas as pd


# series is just like as a list, along with metadata-
# pandas create a default integer index-
# ar1 = pd.Series([1, 2, 3])
# print(ar1)

# datatype is automatically changed by python itself - int64 / float64
# if one element is float in list then the list behaviour will be converted to float nature-
# print(pd.Series( [1, 2, 3, np.nan, 5 data separation(split), 19] ))
# print(pd.Series( [1, 2, 3, 23.00, 5 data separation(split), 19] ))


# # create a dataframe by passing numpy array along with a datatime index & labelled columns:-
# # date in form of - (yyyymmdd)
dates = pd.date_range('20190101', periods=6, freq='D')
# print(dates)

# to access 1st element of the list "dates", but it will also print default time (00:00:00) along with date,
# if we not provide any time :-
print("1st element of the list 'dates-' ", dates[0])
print("\n")


# Note- numpy.random.randn(rows, cols)) :- It creates an random matrix of specified shape & fills it with
# random float values btw 0 & 1, as per "standard normal" distribution, this func. returns a list of rows(lists) in
# the form of matrix on screen. Each list has some values for the columns of matrix.
# print(np.random.randn(6, 4))


# now, we create dataframe (sheet) by using random.randn() --
# index attribute = It is a list of rows
# columns attribute = It is a list of columns
p1 = pd.DataFrame( np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(p1)
# p1 is the dataframe/

# to see the values of any column of dataframe-
print('\n\n', p1['C'])

# to get values of 'A' column only--
print('\n\n', p1.C)


# to get all values row wise -
print('\n\n', p1.loc[dates[0]])           # row 0 is printed
print('\n\n', p1.loc[dates[1]])           # row 1 is printed
print('\n\n', p1.loc[dates[2]])           # row 2 is printed
print('\n\n', p1.loc[dates[3]])           # row 3 is printed
print('\n\n', p1.loc[dates[4]])           # row 4 is printed
print('\n\n', p1.loc[dates[5]])           # row 5 is printed


# to get only one value from the matrix obtained from random.randn() :-
# to get the scaler value ( ie. single value) :-
print( p1.loc[ dates[0], 'A'] )

# to get faster access to the scaler value by using method. (equivalent to above method) :-
# both methods give same scaler value--
print( p1.at[ dates[0], 'A'] )


# select via the position (ie. selection through index) & that position is passed as integers :-
# to get row of 3rd index-
print('\n\n', p1.iloc[3])
# to get data from (3rd & 4th row) & from (0th & 1st) column:--
print('\n\n', p1.iloc[ 3:5, 0:2 ])        # in slicing, end value is not included.
print('\n\n', p1.iloc[ 1:3, : ])


# by giving the index of positions in a list, we can get data from rows & cols-
# in list, all values are included.
print(p1.iloc[ [1, 2, 4], [0, 2] ])      # [1, 2, 4] shows indexes of rows & [0, 2] are indexes of columns


# to get values of (some rows * some col) only-
print('\n\n', p1.loc[ : , ['B', 'C'] ])         # all rows & (B, C) cols

print('\n\n', p1.loc['2019-01-02': '2019-01-05', ['A', 'B']])
print('\n\n', p1.loc['20190102', ['A', 'B']])


# except the numeric data, rest all data like (string/text) are called objects
# to see the column heading having column names-
print("column heading in dataframe-\n", p1.columns)

# to get some column names only from column heading -
print("\n\n", p1.columns[1:3])

# By using slicing, we get data of selected rows only
print('\n\n', p1['2019-01-02': '2019-01-05'])     # here, end row is included


# to print first 3 rows-
print(p1[0:3])


# to see the index column having row names / row headings-
print("row heading in dataframe-\n", p1.index)


# to add new column-
p1['E'] = p1['A'].apply( lambda x : 1 if (x>0) else 0 )
# print("\n", p1['E'])
print('\n\n', p1)


# to group the elements of any column, & print the group along with their frequencies-
print('\n\n', p1.groupby('E').size())

# to see all the values of the matrix only-
# in this method, we can't get column & row heading name-
print("\n\n", p1.values)

# to see all the values of the matrix, along with row name & column name-
# but, here, in this method, we get both column & row heading name-
# here, in this fnx, by default- only first 5 rows are printed
print('\n\n', p1.head())

# to get 3 rows only- give 3 as arg:-
print('\n\n', p1.head(3))

# to get last 5 rows by default-
print('\n\n', p1.tail())

# to get last 3 rows only-
print('\n\n', p1.tail(3))

# Note- head() & tail() func. gives rows along with both col.name & row name
# But, p1.values gives only values but not row & col.name


# to get the datatype of the values of each column
# here, column name along with datatype in dict. form is shown as o/p-
print('\n\n', p1.dtypes)


# sample gives data of any one random row-
print('\n\n', p1.sample())

# but to get data of any no of rows randomly, give that no. as arg.--
print('\n\n', p1.sample(4))       # it gives data of 4 rows by choosing those rows randomly
print('\n\n', p1.sample(2))       # it gives data of 2 rows by choosing those rows randomly


# to get count, std.dev, mean, min, max, %iles(25, 50, 75) of data - use this func.-
print('\n\n', p1.describe())
print('\n\n', p1.describe(include='all') )


# to get transpose of matrix - obtained from random.randn() func.-
# rows <---> colums  (interchanged).   Ex- 3X4 = 4X3
# row name becomes column name & column name becomes row name
print('\n\n', p1.T )

# how to sort-
print('\n\n', p1)
# to sort 'B' column in ascending order-
print('\n\n', p1.sort_values( by='B', ascending=True ))
print()

# to delete any column
# del p1['C']


# to copy the dataframe-
p2 = p1.copy()
print('\n\n', p2)



# Boolean Concept / Boolean Indexing --
# select only those values from dataframe where a boolean condition is met-
# if cond. is true then put True, else put False.
# for full dataframe, cond. is applied-
print('\n\n', p1>0 )

# for any particular column, cond. is applied-
print('\n\n', p1.A > 0)

# Logic- print the value if we got True in [p1>0], else print- NaN
print('\n\n',  p1[p1>0] )                # if cond. is false, then print- NaN
print('\n\n', p1[p1.A > 0])              # if cond. is false, then print nothing

# both cond. in square bracket must be satisfied-
# ie. column "B" is selected & values of col-A must be greater than 0, then print values, else not print them
print('\n\n', p1['B'][ p1.A > 0])

