# data tranformation simpler

# a) rescale - minmaxscaler
# s - standardizescaler
# n = normalizer
# b = binarizer

# rescale use

import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

filename= "indians-diabetes.data.csv"

heading_names = ['preg', 'plas', 'pres',
                 'skin', 'test', 'mass',
                 'pedi', 'age', 'class']


dataframe = pd.read_csv(filename, names=heading_names)


array=dataframe.values
X = array[ : , 0:8 ]
Y = array[ : , 8 ]

scaler = MinMaxScaler( feature_range=(1, 10) )

# rescaledX = scaler.fit_transform(X)

scaler = scaler.fit(X)
rescaledX = scaler.transform(X)

set_printoptions(precision=2)

print(rescaledX [ 0:30, : ])
