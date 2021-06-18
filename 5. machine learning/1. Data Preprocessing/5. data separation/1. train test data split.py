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
model.fit(X_train, Y_train)                   # fiiting the algorithm= means = (training the algorithm by trainng data) 

result = model.score(X_test, Y_test)
print(result)
print( "Accuracy= %.2f %%" % (result * 100) )
