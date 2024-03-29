# There are 4 ways of Feature Selection for Machine Learning: 
# ---------------------------------------------------------------------------------------
#   1. Univariate Feature Selection      ---    SelectKBest  chi2
#   2. Recursive Feature Elimination     ---    coef of corr
#   3. Feature Selection by Principle Component Analysis.(PCA)    ---  explaine var ratio
#   4. Feature Selection by their Importance      ---  gini importnce index
# ---------------------------------------------------------------------------------------


import pandas as pd
from numpy import set_printoptions

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

import warnings
warnings.filterwarnings("ignore")

# load data
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test',
          'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# feature extraction
test = SelectKBest(score_func=chi2, k=3)

fit = test.fit(X, Y)
# summarize scores
set_printoptions(precision=3)
print(fit.scores_)
# print(fit)               # o/p=SelectKBest(k=3, score_func=<function chi2 at 0x00000229287D9318>)
features = fit.transform(X)

# summarize selected features
print("\n\n")
print(features[0:20, :])
