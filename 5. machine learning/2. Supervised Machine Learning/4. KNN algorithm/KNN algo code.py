# poora code glt h

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression


from sklearn.neighbors import KNeighborsClassifier


filename = 'LgR_Movies_kNN_classifier.csv'

# hnames=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
# 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']


dataframe = pd.read_csv(filename)  #, names=hnames)
array = dataframe.values

X = array[: , 1:3]
Y = array[:, 3]

kfold = KFold(n_splits=8 )
# model = LinearRegression()
# scoringMethod = 'neg_mean_absolute_error' #MAE
# results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)
# print( "MAE: %.3f (%.3f)" % ( results.mean(), results.std() ) )


model = KNeighborsClassifier()

results = cross_val_score(model, X, Y, cv=kfold)

print( "Validation Score for kNN : " , results.mean() )
