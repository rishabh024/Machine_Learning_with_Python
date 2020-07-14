# k fold classmethod

# k fold  = k times accuracy of k grps = mean = avg in float value
# jitna traungn data more = utna experivnce jyada hoga m/c ka = more accuracy of model
# divide data into k grps only

# hide 1/10 of data only   &   90% data is used always to get 10 accuracies further clculate mean of 10 accuracies

import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd

from sklearn.model_selection import KFold          # class
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


# results  = advance array of 10 accurcy of 10 grp = given by cross_val_score fnc coz mean to 10 avalue ka hi find hoga na
# tbhi to s laga hai results me to show 10 accurcy , stored in results var
# cross_val_score() is comparratively more powerful than ist method=train test data splt
# 1st me model.score , 2nd method me cross_val_score()
# cross_val_score() fnc ssara kam krega es method me

# kfold value incr => time inc to train algo==> accuracy best aygi = it is best reliable  = not used for billlion amt of data

# a1
# a2
# a3
# a4 ..... a10 = mean of 10 grp ki accuracy = actual avg accracy milegi hume (sare grp ki milakr) in the result as float value only




# 0 0   = 1
# 1 0   = 0
# 0 1   = 0
# 1 1   = 1


print( "results : " , results )
print( "Accuracy: %.2f %%" % ( results.mean()*100.0 ) )


# std dev jitna kam , utna axa = c0z = wo utni relaible h value result  ki-
print( "Std.Deviation= %.2f" % ( results.std()*100.0 ) )



# =====================================================
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
