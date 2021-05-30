import numpy as np
import pandas as pd

import time
import warnings
warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt
from sklearn.externals import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC


print("ML solution proposed by: Rishabh Gupta")
print("Email ID: rishabhgupta2498@gmail.com")
print("Student ID: 372733 ")


data = pd.read_csv('HeartAttack_data.csv', index_col=False)

# The dataset is loaded and now, Exploratory Data Analysis is done

print("\nHeartAttach dataset head() :- \n", data.head())
print("\n columns of dataset :- \n",  data.columns)
print("\n\nShape of the HeartAttach dataset :- ", data.shape)


pd.set_option('display.width', 1000)
pd.set_option('display.max_column', 25)
pd.set_option("precision", 2)

print("\n information about data :- \n", data.info())


data = data.drop(['ca', 'thal', 'slope'], axis=1)
data.replace('?', np.nan, inplace=True)

list_nan_columns = data.isnull().sum()
print("\n\n", list_nan_columns)

data = data.astype('float64')
print("\n\n", data.dtypes)

print("\n\n", data.head(60))
print("\n\n", data.tail(60))


data['trestbps'].fillna((data['trestbps'].median()), inplace=True)
data['chol'].fillna((data['chol'].median()), inplace=True)
data['fbs'].fillna((data['fbs'].median()), inplace=True)
data['restecg'].fillna((data['restecg'].median()), inplace=True)
data['thalach'].fillna((data['thalach'].median()), inplace=True)
data['exang'].fillna((data['exang'].median()), inplace=True)

print("\n\n", data.head(60))
print("\n\n", data.tail(60))

q = data.isnull().sum()
print(q)

print("\n\n", data.dtypes)

print("\n\n", data.skew())

print("\n\n", data.corr())

print("\n\n\n HeartAttack data description :- \n")
print(data.describe(include='all'))

data.hist(figsize=(8, 6))

data.plot(kind='density', subplots=True, layout=(4, 4), sharex=False, legend=False, fontsize=1)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
cax = ax1.imshow(data.corr())
ax1.grid(True)
plt.title('HeartAttack Attributes Correlation')

fig.colorbar(cax, ticks=[.75, .8, .85, .90, .95, 1])
plt.show()

Y = data['num'].values
X = data.drop(['num'], axis=1).values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=180)

models_list = []
models_list.append(('CART', DecisionTreeClassifier()))
models_list.append(('SVM', SVC()))
models_list.append(('NB', GaussianNB()))
models_list.append(('KNN', KNeighborsClassifier()))

num_folds = 10

results = []
names = []

for name, model in models_list:
    kfold = KFold(n_splits=num_folds, random_state=210)
    startTime = time.time()
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    endTime = time.time()
    results.append(cv_results)
    names.append(name)
    print("\n", "%s: %f (%f) (run time: %f)" % (name, cv_results.mean(), cv_results.std(), endTime - startTime))

fig = plt.figure()
fig.suptitle('Performance Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

pipelines = []

pipelines.append(('ScaledCART', Pipeline([('Scaler', StandardScaler()), ('CART', DecisionTreeClassifier())])))
pipelines.append(('ScaledSVM', Pipeline([('Scaler', StandardScaler()), ('SVM', SVC())])))
pipelines.append(('ScaledNB', Pipeline([('Scaler', StandardScaler()), ('NB', GaussianNB())])))
pipelines.append(('ScaledKNN', Pipeline([('Scaler', StandardScaler()), ('KNN', KNeighborsClassifier())])))

results = []
names = []

print("\n\nThe accuracies of algorithm after scaled dataset:- \n")

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    kfold = KFold(n_splits=num_folds, random_state=210)
    for name, model in pipelines:
        start = time.time()
        cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
        end = time.time()
        results.append(cv_results)
        names.append(name)
        print('\n', "%s: %f (%f) (run time: %f)" % (name, cv_results.mean(), cv_results.std(), end - start))


fig = plt.figure()
fig.suptitle('Performance Comparison after scaling the data')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)


model = KNeighborsClassifier(n_neighbors=5)
start = time.time()
model.fit(x_train, y_train)
end = time.time()
x_test = scaler.fit_transform(x_test)
pred_y = model.predict(x_test)


print("\nThe KNN Algorithm is completed. It's Run Time is :- %f" % (end - start))
print('\n', "All the predictions are done successfully by the KNN Algorithm. ")


acc = accuracy_score(y_test, pred_y)
print("\nAccuracy score is:- ", acc*100)


print("\n Confusion_Matrix is :- \n")
print(confusion_matrix(y_test, pred_y))


filename = "finalized_HeartAttach_model.sav"
joblib.dump(model, filename)

print("\n The best performing model is dumped into a file by Joblib successfully.\n")


print("ML solution proposed by: Rishabh Gupta")
print("Email ID: rishabhgupta2498@gmail.com")
print("Student ID: 372733 ")
