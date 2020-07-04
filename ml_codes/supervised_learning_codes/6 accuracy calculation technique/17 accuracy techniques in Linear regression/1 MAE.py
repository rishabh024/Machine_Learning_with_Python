# dots jitna duur, utna error incrses, jitna error badega = more eror more costly
# if distance of dots incrs (variance from mean position increses/ dispersion of dots incrses) from central/mean postion = to error badega
# error are always bad ( chahe neg / pos)
# if proj me error tends to 0 ( or 0) = that proj is good
#
# error can never be 0 by cancellation of +/- sign
# total error evalaute krne ke liye we must neglect sign but consider its magntiude
# sign tells only abt posion / loaction of dots abt best fit line
#
# how to eval. eror with all its mag= 2ways--
# a) sigma | y-y'|==>    to get avg error of all erors = (sigma | y-y'|) / n ==> we call it ==> mean of absolute errors (MAE)
# b) sigma (| y-y'|)^2   ==>    to get avg error of all erors = sigma (| y-y'|)^2 / n ==> we call it ==> mean of squared errors (MsE)
#
# (sigma | y-y'|)/n  == (we also call it avg cost) == sigma (| y-y'|)^2 / n
#
# error is always printed in neg
#
# logistic regresssion has 5 methods == 2 methods tell abt the accuracy of model by evaluating the performance of algo
# & except neg_log_loss mmethod coz it tell the error & 1 method = matrix & other one is- report
#
#
# but in linear regresion- 3w ways = all 3 methods tell abt the errors & not accuracy.
# erros more to accuracy kam
# 1) MAE
# 2) MSE  - zooom / take time --  it is frequently used
# 3) R^2 E

# housing,csv hacing cont. o/p = 4 feature selction colm = 3 data trasbform cols for x , last col=14th col for y


# =============================================================================================================

#  MAE


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

scoringMethod = 'neg_mean_absolute_error' #MAE
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)

print( "MAE: %.3f (%.3f)" % ( results.mean(), results.std() ) )





# =============================================================================================================================


# # Attribute Information:
# # ---------------------------------------------------------------------------
# # 1. CRIM: per capita crime rate by town
# # 2. ZN: proportion of residential land zoned for lots over 25,000 sq.ft.
# # 3. INDUS: proportion of non-retail business acres per town
# # 4. CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
# # 5. NOX: nitric oxides concentration (parts per 10 million)
# # 6. RM: average number of rooms per dwelling
# # 7. AGE: proportion of owner-occupied units built prior to 1940
# # 8. DIS: weighted distances to five Boston employment centres
# # 9. RAD: index of accessibility to radial highways
# # 10. TAX: full-value property-tax rate per 10,000 US Dollars
# # 1 load data. PTRATIO: pupil-teacher ratio by town
# # 2 data visualization. B: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
# # 3 data trasbform. LSTAT: % lower status of the population
# # 4 feature selction. MEDV: Median value of owner-occupied homes in 1000's US Dollars
#
# =============================================================================================================================


# ===============================================================================================================
# 2c-
# Attribute Information:
# ---------------------------------------------------------------------------
# 1. CRIM: per capita crime rate by town
# 2. ZN: proportion of residential land zoned for lots over 25,000 sq.ft.
# 3. INDUS: proportion of non-retail business acres per town
# 4. CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
# 5. NOX: nitric oxides concentration (parts per 10 million)
# 6. RM: average number of rooms per dwelling
# 7. AGE: proportion of owner-occupied units built prior to 1940
# 8. DIS: weighted distances to five Boston employment centres
# 9. RAD: index of accessibility to radial highways
# 10. TAX: full-value property-tax rate per 10,000 US Dollars
# 1 load data. PTRATIO: pupil-teacher ratio by town
# 2 data visualization. B: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
# 3 data trasbform. LSTAT: % lower status of the population
# 4 feature selction. MEDV: Median value of owner-occupied homes in 1000's US Dollars
# ========================================
