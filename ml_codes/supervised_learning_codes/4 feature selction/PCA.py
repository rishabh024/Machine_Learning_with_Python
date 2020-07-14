# Dimension Reduction Method   (PCA method---)
#
# 2col = 2dim data,  7 col = 7 dim data, 85000 col = 85000 dim daata
# dim reduce = reduce that col = col khatam = col ka nos  are dcreased = dim reduction by axis rotaion = data simpler =
# data valueso for one col is reduced to 0 & values of other col will be increased but data pattern is always same=
# x badega 7 y ghatega to 0 = dots remains same = axis change by an angle = best fit line same as dots same
# we do colmn redduction by invreasiing angle/ rotaion   == fir to last me linear data bachega
#
#
# jiska explained var. ratio jyada wo retain  krega  coz of more info retain =  on fit line only  sirf yhi grapf (pc1) bachega= pc2 has more error =  pc2 lkhatam krrgee pehle
#
# date reduce krne se matlab h ki we introdeuce an error , - why we use this conceopt?
# coz  eevn by reduction of col/data amd introduction of some errors;;;; we retain the 95 to  97%  data with min error
# here, min error  is acceptable--
# retain of actual / reral info is calcalte by - -  explained variance= it shows the % of info retained by eeach col
# ex-   Explained Variance: [0.88854663 0.06159078 0.02579012] =
# 1st row=88% info retained
# 2nd rowd has   6% info retained
# 3rdd rowd has   2.5% info retained
#
# total retined info = 88+6+2.5 ~~ 97% info retained with min erroer
#
#



# -----------------------------
import pandas as pd
from sklearn.decomposition import PCA

# load data
filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test',
         'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)

array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]

# feature extraction
pca = PCA(n_components=3)

fit = pca.fit(X)

resultX = pca.transform(X)
print("\nResult : \n", resultX)

# summarize components
print("Explained Variance:", fit.explained_variance_ratio_)
