# how to do data sepaaartion into training data & testing data- & how to evaluate the model
# how to evaluate = divide krke data ko into 4 parts me
# why evaluate the model = coz = how to ensure/trust hte model given nby machine ki wo shi h
#  model ko evaluate kia jaye to find if itt is shi ya galat for to apply model on future data -  eske 4 ways to separate the data  - pehla neeche--


# old/historic data = 100% input & o/p data
# training data (x input data = xtrain & y o/p data= ytrain)  = 67% of old historic data
# testin data = (x input data = xtest & y o/p data= ytest)  = 33% of old historic data


# (10%) or 33 % hidden data ke x per apply krna h model ko = to evalaute the model

# es mehod me biasing nhi hoti h = agr hoti bhi h by chance= then use another 3 methods


# old/historic data = training data +testing data


# a)  train & test set split --
# hume dataset mila usko sep kia = x, y me = esme 4 parts -
# x_test, x_train, y_test, y_train
# xtrain , ytrain = training data= used as i/p data to train the model = to generate program
# xtest, ytest = testing data = trained model is applied on thid data to obtained  (y')
#
# error = y - y'   = (y= ytest=ibtained from nature, manually calculation),
#              (y' = o/p given my machime whne model is apllied to testing data)
# jitna diff jyada utna error  more= utna bekar h model = we cant used it

# in this method , industry acc = 67% data choosen randomly as training data (this data alwsays be more = to train model perfectly with experince)
# baki ka 33%  hide kr diay gya = testing data =   part(1/10) to part(1/3) is hidden


# imp imp imp imp imp imp --- model is always applied on the part of x ie xtest data
# but model never applied on the ytest data coz ytest data used for cross check &  geting error by comparison from y' = y' given by model

# data for test/train purpose is choosen randomly
# coz jaruri nhi h ki modeule kaam krega if we take (starting/ending/middle) data so we take random data lenge from entire dtataset

# dobara run krne per we get diff o/p as we take true random data
# randomly choosen data of (33% & 67%)  is stored in new dataset
# best fit model = the best model is produced by fit fnc = thats why model is called best fit model.
# best fit modell me h best line = so this line is called as best fit line

# best fit line has= minimum dispersion/variance from mean/ central position = es cas me = information is retained with high % & less error



# test train data split-- method

import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

# Note - logistic regression/classification  is applied for dicrete categorical o/p = for class col

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
# x = input data = go ot x array
X = array[: ,0:8]

# y = output data = go ot y array
Y = array[: , 8]


# used t oget test data = laways choose in float value & not in %
test_data_size = 0.33
#seed = 8

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=test_data_size )

# ,random_state=seed
model = LogisticRegression()
model.fit(X_train, Y_train)
# fiiting the algorithm= means = (training the algorithm by trainng data) = es trained model ki accuracy is caluaculated by score fnx-
# fit () gives trained model by taking training data and = calculate parametrs(m,c) of the model/best fit line = we also get eq = that eq is also called as by 6 names - model/algo
# after getting trained model, we get best fit line = es line ki eq shown by its paarameters(m,c) = { y = mx+c}


# es method ka sara kam score fnx krega = y' calcutate / compare matching hoga for error
# score fnx model ko apply kregha on xtest to produce y' = bad me compare matching hoga for error and give result
# result yh btayga ki kitna % accurate h  machine ka model  = result me = accuracy aygi = in float value coz sari values float me hi di gyi h = return bhi float me hi hogi



# if accuracy of model is 100%- it guaranyees taht our algo is 100% wrong = highest chance that ki wo model not work on furure data = eska concept is called over fittting
# over fitting ka matlab hai = over trained kr diya h model ko = (fit means =train)
# underfitting  means kam trained kia h model ko
#  overfitting  means jyada trained kia h model ko


result = model.score(X_test, Y_test)
print(result)
print( "Accuracy= %.2f %%" % (result * 100) )

# disadvantage of train test data split===
#we not use 67 % as test data ( model not tested on 67% data) = (it means ho skta h model may/may not work on 67% data) = 67% dta not tested & not verified
# this drwaback remove in next 3 ways of separation od data & eval of algo



# tarin test data split method = its advanced version hai = repeated random train test splits
# k-fold methos - ka advanced version hai  = leave one ot cross validation method
# LeaveOneOutcross val = is speacila version of kfold technique





# ========================================================================================
#
# import warnings
# warnings.filterwarnings(action="ignore")
#
# import pandas as pd
#
# from sklearn.model_selection import KFold
# from sklearn.model_selection import cross_val_score
#
# from sklearn.linear_model import LogisticRegression
# filename = 'indians-diabetes.data.csv'
#
# hnames = ['preg', 'plas', 'pres', 'skin', 'test',
# 'mass', 'pedi', 'age', 'class']
#
# dataframe = pd.read_csv(filename, names=hnames)
# array = dataframe.values
# X = array[:,0:8]
# Y = array[:,8]
#
# model = LogisticRegression()
#
# num_folds = 10
# kfold = KFold(n_splits=num_folds)
# results = cross_val_score(model, X, Y, cv=kfold )
#
# print( "results : " , results )
#
#
# print( "Accuracy: %.2f %%" % ( results.mean()*100.0 ) )
#
# print( "Std.Deviation= %.2f" % ( results.std()*100.0 ) )
#
#
#
