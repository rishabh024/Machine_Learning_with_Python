

import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
data = pd.read_csv('LinearRegression5_Data.csv')
print(data)

print(data.shape) #(6,2)

X = data.iloc[ : , 0:1].values                      # [ rows , cols ]
y = data.iloc[:, 1].values

print("X.shape = ", X.shape , "\n X=\n" , X)

print("y.shape = ", y.shape , "\n y=" , y )


from sklearn.linear_model import LinearRegression

lin = LinearRegression()
lin.fit(X, y)
y_dash = lin.predict(X)

plt.scatter(X, y, color='blue')
plt.plot(X, y_dash , color='red')
plt.title('Linear Regression')
plt.xlabel('Engine Temperature')
plt.ylabel('Engine Pressure')

plt.show()

# ========================================

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)

#poly.fit(X_poly, y)
lin2 = LinearRegression()
lin2.fit(X_poly, y)


plt.scatter(X, y, color='blue')

plt.plot(X, lin2.predict(poly.fit_transform(X)), color='red')
plt.title('Polynomial Regression')
plt.xlabel('Engine Temperature')
plt.ylabel('Engine Pressure')

plt.show()





# Predicting a new result with Linear Regression
print( "LinearRegresion: ", lin.predict([[110.0]]) )

# Predicting a new result with Polynomial Regression
print( "PolynomialRegresion: ",lin2.predict(poly.fit_transform([[110.0]])) )



# # ========================================
#
#
# import matplotlib.pyplot as plt
# import pandas as pd3
#
# # Importing the dataset
# data = pd.read_csv('LinearRegression5_Data.csv')
# print(data)
#
# print(data.shape) #(6,2)
#
# X = data.iloc[ : , 0:1].values # [ rows , cols ]
# y = data.iloc[:, 1].values
#
# print("X.shape = ", X.shape , "\n X=\n" , X)
#
# print("y.shape = ", y.shape , "\n y=" , y )
#
#
# from sklearn.linear_model import LinearRegression
#
# lin = LinearRegression()
# lin.fit(X, y)
# y_dash = lin.predict(X)
#
# plt.scatter(X, y, color='blue')
# plt.plot(X, y_dash , color='red')
# plt.title('Linear Regression')
# plt.xlabel('Engine Temperature')
# plt.ylabel('Engine Pressure')
#
# plt.show()
# from sklearn.preprocessing import PolynomialFeatures
#
# poly = PolynomialFeatures(degree=4)
# X_poly = poly.fit_transform(X)
#
# #poly.fit(X_poly, y)
# lin2 = LinearRegression()
# lin2.fit(X_poly, y)
#
#
# plt.scatter(X, y, color='blue')
#
# plt.plot(X, lin2.predict(poly.fit_transform(X)), color='red')
# plt.title('Polynomial Regression')
# plt.xlabel('Engine Temperature')
# plt.ylabel('Engine Pressure')
#
# plt.show()
#




# ========================================
# 4c-
#
#
# # -*- coding: utf-8 -*-
# """
# Created on Fri Jun 19 19:6 accuracy calculation technique:2 data visualization 2020
#
# @author: sai ujwal vangapally
# """
#
# # Spot-Check of Machine Learning Algorithms
# #--------------------------------------------------
#
# #1)Logistic Regression.
# #2)Linear Discriminant Analysis(LDA).
# #3)k-Nearest Neighbors (kNN).
# #4)Naive Bayes (=NB = GaussianNB).
# #5)Classification and Regression Trees(CART).
# #6)Support Vector Machines (SVM).
# import warnings
# warnings.filterwarnings(action="ignore")
#
# import pandas as pd
# from sklearn.model_selection import KFold
# from sklearn.model_selection import cross_val_score
#
# filename = 'indians-diabetes.data.csv'
# headingNames = ['preg', 'plas', 'pres',
# 'skin', 'test', 'mass',
# 'pedi', 'age', 'class']
#
# dataframe = pd.read_csv(filename, names=headingNames)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# kfold = KFold(n_splits=10)
#
# #1) Spot cheching for Logistic Regression
# #---------------------------------------------------------
# from sklearn.linear_mo
#
#
# ========================================
# 4c-
#
# #6)Spot cheching for Support Vector Machines ( SVM )
# #----------------------------------------------------------------------------------------
# #SVM seek a line that best separates two classes.
# # Those data instances that are closest to the line that
# # best separates the classes are called support vectors
# # and influence where the line is placed.
#
# from sklearn.svm import SVC
# model = SVC()
# results = cross_val_score(model, X, Y, cv=kfold)
# print( "Validation Score for SVM : ", results.mean())
#
#
#
# ========================================