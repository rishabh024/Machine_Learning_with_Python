# KFold method

import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd

from sklearn.model_selection import KFold        # class
from sklearn.model_selection import cross_val_score            # variable

from sklearn.linear_model import LogisticRegression
filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test',
'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

model = LogisticRegression()

num_folds = 10
kfold = KFold(n_splits=num_folds)
results = cross_val_score(model, X, Y, cv=kfold )         # cv = cross validation


print( "results : " , results )
print( "Accuracy: %.2f %%" % ( results.mean()*100.0 ) )

# std dev jitna kam , utna axa = c0z = wo utni relaible h value result  ki-
print( "Std.Deviation= %.2f" % ( results.std()*100.0 ) )
