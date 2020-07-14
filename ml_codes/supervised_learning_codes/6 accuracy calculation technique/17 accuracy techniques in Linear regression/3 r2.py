# std dev= it tells that how many dots/elements are deviated/dispersed/scattered (bikhare huye)
# (ie jo jitna dur hai/ dots which are far away/ jin dots ki distance jyda h from best fit line) from mean/central position,
# en sb me error jyada hoga jinki distance jyada hai
#
#
# jin dots ki distance kam h from best fit line unme error kam hoga - it is good for proj
#
#
# std dev ka ulta hota h in r^2 method me--
# std dev tell abt the farness of dots from central pos/best fit line  &
# but, r2 method tell abt the closeness of dots from central pos/best fit line
#
# r2 ki value ki range is btw 0 & 1 like probabiltiy
#
# r2 = 100% =1 when closenss max = std dev  = 0 = duriyaaan = 0 ho gyi
#
#
# duriyan =1= 100% = r2 is 0
# error tend to 0% = 0 = duriyan is min = 0
# closeness tends to 1 =100%
#
# =========================================================================================================
#
# r2 tell clsoenss of dots = 100% = 1  = or tends to 1 value
#
#
#
# v.v.v. imp--->jitna dots pass me hogi, utna kam error hoga  = utna hi axa hoga model
# v.v.v. imp---> jitna duri kam/ jitni pass dota hogi = utna kam error = utna hi axa hoga model
# std dev is reciprocal of r2
# kosis = dots must approch to best fit line = duriya kam = closenss = 100%
# duriyan kam hogi by faeture selction/ data tranform krke duriyan kam kre
#
#
# if o/p in r2 me = 0.2038494 = tends to 0  = dots jyada bikhri hai = yh shi nhi h o/p for proj coz error bar gaya
# if o/p in r2 me = 0.9472387 = tends to 1  = yh shi h o/p for proj coz error ghat gaya
#
#
#
# if we talk abt std dev - gives distanve/duriyan of dots = std dev ki value must tands to 0  value
# if o/p of  std dev  is = 0.2038494 = tends to 0  = yh shi h o/p for proj coz error ghat gaya
# if o/p of  std dev  is = 0.9472387 = tends to 1  = yh shi nhi h o/p for proj coz error bar gaya
#
#


#  ============================================================================================================


# r^2 errror

from pandas import read_csv
import warnings
warnings.filterwarnings(action="ignore")
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

filename = 'housing.csv'
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
dataframe = read_csv(filename, names=names)

array = dataframe.values
X = array[:,0:13]
Y = array[:,13]

kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = LinearRegression()
scoringMethod = "r2"
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod )

print("R2: %.3f" % ( results.mean() ) )

