# understanding the data visualization:--
#
# b) Multivariate Plots:- It is applied in 2 ways-
#   1) Correlation Matrix Plot
#   2) Scatter Matrix Plot

# Now, we use Correlation Matrix Plot--

# Correlation gives the indication of how the changes are related between two variables:--
# If 2 variables change in same direction, then they are correlated positively.
# If 2 variables change in opposite direction, (ie. one goes up & one hoes down) then they are correlated negatively.
# those dots which are very close to each other, possesses high correlation with each other.


import warnings
warnings.filterwarnings(action='ignore')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

heading_names = ['preg', 'plas', 'pres',
                 'skin', 'test', 'mass',
                 'pedi', 'age', 'class']

dataframe = pd.read_csv("indians-diabetes.data.csv", names=heading_names)

pd.set_option("display.width", 1000)
pd.set_option("display.max_column", 9)


# by default, method is- pearson
correlations = dataframe.corr()
print(correlations)

# Correlation Matrix Plot--

fig = plt.figure()
subfig = fig.add_subplot(111)


# matshow means - matrix show
# vmin & vmax is used to show the scale length--
# diagonal cells in matrix are useless.
# colorbar is used to represent the scale/bar of matrix--


# matshow fnc will add matrix in subplot area
cax = subfig.matshow(correlations, vmin=-1, vmax=1)

# colorbar fnc will add sidebar to the matrix
fig.colorbar(cax)


ticks = np.arange(0,9)
subfig.set_xticks(ticks)
subfig.set_yticks(ticks)

# if we not use set_xticklabels & set_yticklabels methods, then 0- 8 nos are printed on the axis of graph.
# we shouls use set_xticklabels & set_yticklabels methods, to represent the ticks with the names-printed on the axis
# x_label & y_label is used to represent the axis names

subfig.set_xticklabels(heading_names)
subfig.set_yticklabels(heading_names)

plt.show()
