# Now, we use Univariate Density Plot to understand each attribute/column of the dataset--

import matplotlib.pyplot as plt
import pandas as pd

filename = "indians-diabetes.data.csv"
heading_names = ['preg', 'plas', 'pres',
                 'skin', 'test', 'mass',
                 'pedi', 'age', 'class']


dataframe = pd.read_csv(filename, names=heading_names)

# to draw Univariate density plot, use "density" in kind argument--

# sharex arg.- if we want to share the values of x to each subplot, then we make it True,
# else make it False as--> not to share the values of x with each subplot in the figure

# layout arg.- it takes tuple as(rows, cols):-
# Ex-
# dataframe.plot(kind='density', subplots=True, layout=(9, 1), sharex=False)
# dataframe.plot(kind='density', subplots=True, layout=(9, 1), sharex=True)
# dataframe.plot(kind='density', subplots=True, layout=(2, 5), sharex=False)

# if subplots arg. is False then all plots will be represented in one figure only-
# dataframe.plot(kind='density', subplots=False, layout=(3, 3), sharex=False)

dataframe.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)

plt.show()
