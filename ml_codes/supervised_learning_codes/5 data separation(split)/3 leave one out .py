# LeaveOneOutcross val = is speacila version of kfold technique
# hide 1 grp only
# it ie worst in terms of time        so we use it for small amt of data only-
# it is best in terms if accuracy
# tottal k fold = total no of rows




import warnings
warnings.filterwarnings(action="ignore")
from pandas import read_csv
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test',
'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]


loocv = LeaveOneOut()
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=loocv)

print( "results : " , results )

print( "result.size : " , results.size )

print( "Sum of Positive Results: %i " % (
results.sum() ) )

print( "Accuracy= %.2f %%" % (
results.sum() * 100 / results.size ) )


#  1 means ( y & y' )exactly matching   = sum
#  0  means ( y & y') not matching

# # =========================================================
# #3rd method
# import warnings
# warnings.filterwarnings(action="ignore")
# from pandas import read_csv
# from sklearn.model_selection import LeaveOneOut
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
#
# filename = 'indians-diabetes.data.csv'
# names = ['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
#
# dataframe = read_csv(filename, names=names)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# loocv = LeaveOneOut()
# model = LogisticRegression()
# results = cross_val_score(model, X, Y, cv=loocv)
#
# print( "results : " , results )
#
# print( "result.size : " , results.size )
#
# print( "Sum of Positive Results: %i " % (
# results.sum() ) )
#
# print( "Accuracy= %.2f %%" % (
# results.sum() * 100 / results.size ) )
#
#
