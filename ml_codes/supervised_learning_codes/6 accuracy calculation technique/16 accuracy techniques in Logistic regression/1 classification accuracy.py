# 1c

# 1) Cross Validation Classification Accuracy
import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

filename = 'indians-diabetes.data.csv'
names=['preg', 'plas', 'pres', 'skin',
'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=names)

array = dataframe.values
X = array[: , 0:8]
Y = array[:,8]

kfold = KFold(n_splits=10 )
model = LogisticRegression()

# This is the default method of accuracy
scoringMethod = 'accuracy'


results = cross_val_score( model, X, Y,cv=kfold , scoring=scoringMethod )

print( "Accuracy: %.3f , dev is-, (%.3f)" % ( results.mean()*100, results.std()*100 ) )


# ========================================
# 2c-
#
# #A.2) Cross Validation using Classification LogLoss
# import pandas as pd
# from sklearn.model_selection import KFold
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
#
# import warnings
# warnings.filterwarnings(action='ignore')
#
# filename = 'indians-diabetes.data.csv'
# names=['preg', 'plas', 'pres', 'skin',
# 'test', 'mass', 'pedi', 'age', 'class']
# dataframe = pd.read_csv(filename, names=names)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# kfold = KFold(n_splits=10)
# model = LogisticRegression()
#
# scoringMethod = 'neg_log_loss'
#
# results=cross_val_score( model, X, Y, cv=kfold,
# scoring=scoringMethod)
#
# print("Logloss: %.3f (%.3f)" %(results.mean(), results.std() ) )
#
# ========================================
# 3c-
#
#
# import warnings
# warnings.filterwarnings(action="ignore")
#
#
# from pandas import read_csv
# from sklearn.model_selection import KFold
# from sklearn.model_selection import cross_val_score
#
# from sklearn.linear_model import LogisticRegression
# filename = 'indians-diabetes.data.csv'
# names=['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
# dataframe = read_csv(filename, names=names)
#
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
# kfold = KFold(n_splits=10 )
#
# model = LogisticRegression()
#
# scoringMethod = 'roc_auc'
#
# results = cross_val_score(
# model, X, Y, cv=kfold, scoring=scoringMethod)
#
# print("AUC: %.3f (%.3f)" % (
# results.mean()*100, results.std()*100 ) )
#
#
# ========================================
# 4c-
#
# import warnings
# warnings.filterwarnings(action="ignore")
#
#
# from pandas import read_csv
# from sklearn.model_selection import KFold
# from sklearn.model_selection import cross_val_score
#
# from sklearn.linear_model import LogisticRegression
# filename = 'indians-diabetes.data.csv'
# names=['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
# dataframe = read_csv(filename, names=names)
#
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
# kfold = KFold(n_splits=10 )
#
# model = LogisticRegression()
#
# scoringMethod = 'roc_auc'
#
# results = cross_val_score(
# model, X, Y, cv=kfold, scoring=scoringMethod)
#
# print("AUC: %.3f (%.3f)" % (
# results.mean()*100, results.std()*100 ) )
#
