# Now, we use Univariate Box & Whisker Plot to understand each attribute/column of the dataset--

import matplotlib.pyplot as plt
import pandas as pd

filename = "indians-diabetes.data.csv"
heading_names = ['preg', 'plas', 'pres',
                 'skin', 'test', 'mass',
                 'pedi', 'age', 'class']


dataframe = pd.read_csv(filename, names=heading_names)

dataframe.plot(kind='box', subplots=True, layout=(3, 3), sharex=False)

plt.show()
