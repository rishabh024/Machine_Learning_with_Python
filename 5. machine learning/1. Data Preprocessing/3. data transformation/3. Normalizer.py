# Normalizer-

from sklearn.preprocessing import Normalizer
from pandas import read_csv
from numpy import set_printoptions
import numpy as np


filename= "indians-diabetes.data.csv"

heading_names = ['preg', 'plas', 'pres',
                 'skin', 'test', 'mass',
                 'pedi', 'age', 'class']


dataframe = read_csv(filename, names=heading_names)

array=dataframe.values
X = array[ : , 0:8 ]
Y = array[ : , 8 ]

scaler = Normalizer()
normalizedX = scaler.fit_transform(X)

set_printoptions(precision=2)
print(normalizedX[:30, :])

print("\nmean-\n", np.mean(normalizedX[:, 0]))
