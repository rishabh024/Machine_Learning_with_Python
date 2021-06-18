# understanding the data visualization:--

# It is done in two ways-
# a) Univariate plots
# b) Multivariate Plots


# a) - Univariate plots:-
# In this section, we will look at three techniques which is used to understand each attribute/column of
# the dataframe/dataset independently:-
# 1) Univariate Histogram Plot
# 2) Univariate Density Plot
# 3) Univariate Box & Whisker Plot

# Now, we use Univariate Histogram Plot:-

import matplotlib.pyplot as plt
import pandas as pd

filename = "indians-diabetes.data.csv"
heading_names = ['preg', 'plas', 'pres',
                 'skin', 'test', 'mass',
                 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=heading_names)

print(dataframe)

# to draw histogram-
dataframe.hist()
plt.show()
