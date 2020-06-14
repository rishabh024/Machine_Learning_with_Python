# Now, we use Scatter Matrix Plot for data visualization of the dataset--

# Drawing all the scatter plots together is called a Scatter Matrix Plot

import numpy as np

import warnings
warnings.filterwarnings(action='ignore')

# scatter_matrix is imported to draw scatter matrix plot

import matplotlib.pyplot as plt
from pandas import read_csv
from pandas.plotting import scatter_matrix


heading_names = ['preg', 'plas', 'pres',
                 'skin', 'test', 'mass',
                 'pedi', 'age', 'class']


# since we have import read_csv fnc, so we used it direclty without any type of calling.
dataframe = read_csv("indians-diabetes.data.csv", names=heading_names)

scatter_matrix(dataframe)
plt.show()
