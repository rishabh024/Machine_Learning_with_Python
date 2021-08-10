<h1><p>Machine Learning</p></h1>
<p align="center"><img src="/imgs/machine learning.PNG" height="370" width="770"><br></p>
<h3>It is the repository contaiing all the work that I had done in my ML Training</h3>

<br>

##  Categories of Machine Learning:	

* **Supervised Machine Learning**
Here, we have labeled data ie. we have both input feature variables and output feature variables and we will trained the model with the help of labeled data. There are two types of Supervised Machine Learning techniques:
  > + Regression Machine Learning: <br>
      In Regression, the target attribute is present in the form of continuous output. This regression technique    
      is used to fit the data and predict the values of a desired continuous attribute.
  > + Classification Machine Learning:<br>
      In classification, the target attribute exists in the form of discrete finite output. It is used to specify   
      the class to which input feature variable belongs to.

* **Unsupervised Machine Learning**
Here, we have unlabeled data ie. only input feature variable exists in the dataset and this technique is used to identify the common characteristics in the dataset and forms the clusters and finds that the data point falls into which group or cluster.

* **Reinforcement Machine Learning**
In it, the machine learns itself how to behave in the environment by performing the actions and also determines the best possible action on the basis of rewards or punishments.

<br>

## Steps to build the ML application
<img src="/imgs/steps.PNG" height="310" width="713">

<br>

## Data Preprocessing

* **Data Loading**
We can import the dataset by using pd.read_csv()

* **Data Visualization**
We can analysed the relationship exists between the attributes of different data objects in the dataset by using multivariate and univariate plottings

* **Data Transformation**
Sometimes, data is not available in the right format to use it for the training purpose so it requires the transformation to make it more useful for the training.

* **Feature Selection**
It is also called variable selection or attribute selection. It is the process of reducing the number of input variables by selecting those attributes in the dataset that are most relevant and have the strong relationship with the target variable. By using feature selection methods, we can identify and remove unneeded, irrelevant and redundant attributes from dataset that do not contribute to the accuracy of a predictive model or may decrease the accuracy of the model. This process is done to reduce the computational cost of modeling and to improve the
performance of the model.

* **Data Separation**
We split the dataset into two parts:
a. Training dataset - a subset to train the model.
b. Testing dataset - a subset to test the trained model.
Testing of trained model is also done to check if it is feasible to use that particular model on
the unseen future data or not.

<br>

## Various Machine Learning algorithms

* **Linear Regression**
It is used to find the linear relationship between the independent(x) and dependent(y) variable so that we can predict a dependent variable value (y) based on a given independent variable (x).
<img src="/imgs/Linear regression.PNG" height="310" width="450">
<br>

* **Logistic Regression**
It is used to specify the class of input feature variable. In it, the target attribute exists in the form of discrete finite output.
<img src="/imgs/logistic regression.PNG" height="310" width="450">
<br>

* **decision tree**
It is a binary tree in which each branch node represents a single input variable (x) and each leaf node of the tree contain an output variable (y) which is used to make a prediction. It is also called as classification and regression tree (CART).
<img src="/imgs/decision tree.jpg" height="310" width="450">
<br>

* **Gaussian Naive Bayes Classifier**
It is a kind of classifier that works on Bayes theorem which tells the probability of something, which will happen, given that something else has already occurred. Here, the posterior probability of each class is calculated. The class with higher posterior probability is the output of the prediction.
<img src="/imgs/gnb.PNG" height="310" width="450">
<br>

* **kmeans clustering**
K-Means Clustering is an iterative algorithm that divides the unlabeled dataset into k different clusters in such a way that each dataset belongs only one group that has similar properties.
<img src="/imgs/kmeans clustering.png" height="310" width="450">
<br>

* **knn**
In this algorithm, to classify the unlabeled object, the distance of this object to all the labelled objects is evaluated and its k- nearest neighbors are identified and the class label of the majority of nearest neighbors is used to determine the class of the unlabeled data. Euclidean distance between 2 data points: sqrt( (x2-x1)^2 + (y2-y1)^2 )
<img src="/imgs/knn.png" height="310" width="450">
<br>

* **svm**
This algorithm is used to create the best decision boundary line, also called a hyperplane, that can separate n-dimensional space into different classes so that we can put the new future data point in the correct category easily.
<img src="/imgs/svm.jpg" height="310" width="450">

<br>

## Accuracy of Machine Learning model
In terms of linear regression, accuracy is evaluating the performance of the model by finding that how much the predicted results by the model, are near to the actual value of future unseen dataset. In terms of logistic regression, accuracy is the percentage of classifying the objects of different classes correctly.
<br>
<br>
Three accuracy techniques used in linear regression are:
  > + a. Mean absolute error (MAE)
  > + b. Mean square error (MSE)
  > + c. R2 error  

Five accuracy techniques used in logistic regression are:
  > + a. Classifction accuracy
  > + b. Neg_log_loss
  > + c. Area under ROC
  > + d. Confusion matrix
  > + e. Classification report
