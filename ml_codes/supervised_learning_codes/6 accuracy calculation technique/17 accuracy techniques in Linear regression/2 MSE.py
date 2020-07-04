
# shuffle is false by default = ie generation of random no is fixed = random_state = 7/seed ,       (seed =7)
# if shuffle is true = ie generation of random no is not  fixed
# alwasy advisable to use random data from dataset in project = eske liye we must do --> shuufle=true
#
# ====================================================================================================================
# mse zoom krke dega  o/p esliye frequently use kia jata ah es method ko




# MSE
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

filename = 'housing.csv'

hnames=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[: , 0:13]
Y = array[:,13]

kfold = KFold(n_splits=10 )
model = LinearRegression()

scoringMethod = 'neg_mean_squared_error'           #MSE
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)

print( "MSE: %.3f (%.3f)" % ( results.mean(), results.std() ) )
