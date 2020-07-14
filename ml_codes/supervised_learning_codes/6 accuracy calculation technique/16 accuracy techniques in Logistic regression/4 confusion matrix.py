# 141  41        all element sum =254
# 21   51          # 33% of 768 = 254 eska matlb h ki jo matrix mili = o/p as a matrix= matrix is report off 33% of historic data
#                  # why 33% = coz test_size is give an 0.33 in float esliye we get 33 % of historic data
# 1st conclusion-  # real fact = 33% is of testing data & not of historic data
#                  # coz =33% daata hidem so , we get accuracy 33% = when we apply model on 33$ testing data
#
# 2ns onculsion = we get dffrent o/p on deffirnt computers= values of matric will change but sum of all elem of matrix =alwasy fixed/same hoga
#
#
# 3rd conclusion--
# *
#   *
#      *
#        *          # not divitc person = 0    & machine also tell not dibitc = 9 (141, 51)     o.p =1 ==>>  # machine work well
#
#
# 41 = =  mach ne kha ki dibitc hai person = 1  & but real me person not divitic =0   = o/p ==>> 0   ==> #  # machine not work well
# 21  is inverse of 41 case == o/p ==>> 0   ==> #  # machine not work well
#
#
#
# 141 &n51  can be big values in digonal &    [21 & 41 must be small values ]   for good model/algo = 7 & algo work well
# agr uper values ka reverse hua then algo is not work well
#
#
#
# 4th conclusiion-
# this confusion  matric use ceil function


#A.4) Cross Validation Classification Confusion Matrix

import warnings
warnings.simplefilter(action="ignore", category=Warning)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

filename = 'indians-diabetes.data.csv'
names=['preg', 'plas', 'pres', 'skin', 'test',
'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

test_size = 0.33
#seed = 7
#,random_state=seed

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=test_size )

model = LogisticRegression()
model.fit(X_train, Y_train) # m , c

predicted = model.predict(X_test) # y --> sigmoid


matrix = confusion_matrix(Y_test, predicted)

print(matrix)






# ===========================================================================================================
# import warnings
# warnings.simplefilter(action="ignore", category=Warning)
#
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report
#
# filename = 'indians-diabetes.data.csv'
# names=['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
#
# dataframe = pd.read_csv(filename, names=names)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# test_size = 0.33
# seed = 7
#
#
# X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=test_size, random_state=seed )
#
# model = LogisticRegression()
# model.fit(X_train, Y_train) # m , c
#
# predicted = model.predict(X_test) # y --> sigmoid
#
#
# report = classification_report(Y_test, predicted)
#
# print(report)

# ===================================================================================
#
# #A.4) Cross Validation Classification Confusion Matrix
#
# import warnings
# warnings.simplefilter(action="ignore", category=Warning)
#
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix
#
# filename = 'indians-diabetes.data.csv'
# names=['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
#
# dataframe = pd.read_csv(filename, names=names)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# test_size = 0.33
# #seed = 7
# #,random_state=seed
#
# X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=test_size )
#
# model = LogisticRegression()
# model.fit(X_train, Y_train) # m , c
#
# predicted = model.predict(X_test) # y --> sigmoid
#
#
# matrix = confusion_matrix(Y_test, predicted)
#
# print(matrix)
# =============================================================================================
#A.4) Cross Validation Classification Confusion Matrix
#
# import warnings
# warnings.simplefilter(action="ignore", category=Warning)
#
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix
#
# filename = 'indians-diabetes.data.csv'
# names=['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
#
# dataframe = pd.read_csv(filename, names=names)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# test_size = 0.33
# #seed = 7
# #,random_state=seed
#
# X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=test_size )
#
# model = LogisticRegression()
# model.fit(X_train, Y_train) # m , c
#
# predicted = model.predict(X_test) # y --> sigmoid
#
#
# matrix = confusion_matrix(Y_test, predicted)
#
# print(matrix)
#  ===========================================================================================

#A.4) Cross Validation Classification Confusion Matrix

# import warnings
# warnings.simplefilter(action="ignore", category=Warning)
#
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix
#
# filename = 'indians-diabetes.data.csv'
# names=['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
#
# dataframe = pd.read_csv(filename, names=names)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# test_size = 0.33
# #seed = 7
# #,random_state=seed
#
# X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=test_size )
#
# model = LogisticRegression()
# model.fit(X_train, Y_train) # m , c
#
# predicted = model.predict(X_test) # y --> sigmoid
#
#
# matrix = confusion_matrix(Y_test, predicted)
#
# print(matrix)
# ========================================
# 6c-
#
# #A.4) Cross Validation Classification Confusion Matrix
#
# import warnings
# warnings.simplefilter(action="ignore", category=Warning)
#
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix
#
# filename = 'indians-diabetes.data.csv'
# names=['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
#
# dataframe = pd.read_csv(filename, names=names)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# test_size = 0.33
# #seed = 7
# #,random_state=seed
#
# X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=test_size )
#
# model = LogisticRegression()
# model.fit(X_train, Y_train) # m , c
#
# predicted = model.predict(X_test) # y --> sigmoid
#
#
# matrix = confusion_matrix(Y_test, predicted)
#
# print(matrix)
