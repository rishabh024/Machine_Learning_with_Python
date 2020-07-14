# Feature Selection for Machine Learning: 4 Ways
# -----------------------------------------------
#   1. Univariate Feature Selection.   --- SelectKBest  chi2
#   2. Recursive Feature Elimination.  ---  coef of corr
#   3. Feature Selection by Principle Component Analysis.(PCA) - ---  explaine var ratio
#   4. Feature Selection by their   Importance.              - gini importnce index
# -----------------------------------------------


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

# since k = 3 best col are selected for o/p as top 3 rankings are provided to the cols on the basis of chi^2 technique
# top3 rankings are displayed as 1 1 1 2 3 4 5...

# since k = 5 best col are selected for o/p as top 5 rankings are provided to the cols on the basis of chi^2 technique
# top 5 rankings are displayed as 1 1 1 1 1 2 3 4 5...

# since k = 3 data trasbform best col are selected for o/p as top 3 data trasbform rankings are provided to the cols on the basis of chi^2 technique
# top 3 data trasbform rankings are displayed as 1 1 1 1111111111 2 3 4 5...

# since k = 990 best col are selected for o/p as top 990 rankings are provided to the cols on the basis of chi^2 technique
# top 990 rankings are displayed as 1 1 1......   2 3 4 5...


fit = test.fit(X, Y)
# summarize scores
set_printoptions(precision=3)
print(fit.scores_)
# print(fit)               # o/p=SelectKBest(k=3, score_func=<function chi2 at 0x00000229287D9318>)
features = fit.transform(X)

# summarize selected features
print("\n\n")
print(features[0:20, :])
