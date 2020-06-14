# To estimate the coefficient of correlation with the help of these methods-
# a) Scatter diagram method
# b) Karl Pearson's Method of coefficient of Correlation
# c) Spearman Rank's Coefficient correlation
# d) By Kendall Method


import pandas as pd

filename = "indians-diabetes.data.csv"

heading_names = ['preg', 'plas', 'pres',
                 'skin', 'test', 'mass',
                 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=heading_names)

# review the first 10 rows of data by using head fnc of pandas dataframe-
print("first 10 rows-\n",dataframe.head(10))
print('*'.center(20, '-'))           # The fill character must be exactly one character long

# dimensions of your data
print("shape-", dataframe.shape)
print('*'.center(20, '-'))

# datatype of each attribute / column_name/ heading_name
print(dataframe.dtypes)
print('*'.center(20, '-'))


pd.set_option("display.width", 1000)
pd.set_option("precision", 2)
print('*'.center(20, '-'))

# Descriptive Statistics-
print("description-", dataframe.describe())
print('*'.center(20, '-'))


class_col_counts = dataframe.groupby('class').size()
print(class_col_counts)

# Note- The fill character must be exactly one character long
# print('*'.center(20, '-*-'))     # error occurred
print('*'.center(20, '-'))


# Correlations between the attributes:--
# Correlation refers to the relationship exists between two variables
# how they may/may not change together to describe the relationship

# Karl Pearson;s method to estimate correlation:-
# value of the coefficient of correlation varies from (-1 to +1)
# method must be either 'pearson', 'spearman', 'kendall'

# note- diagonal values are useless

correlations = dataframe.corr(method='pearson')
print('\npearson--\n', correlations)
print("-*-"*20)

correlations = dataframe.corr(method='spearman')
print('\nspearman--\n', correlations)
print("-*-"*20)

correlations = dataframe.corr(method='kendall')
print('\nkendall--\n', correlations)
