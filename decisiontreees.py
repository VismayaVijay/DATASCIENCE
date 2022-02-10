#to implement decision tree using any standard dataset available in the public domain and find the accuracy of the algorithm


import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus


data=load_iris()
print(data.data.shape)
print('classes to predict:',data.target_names)


X= data.data
y=data.target


print(display (X.shape,y.shape))
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 50, test_size=0.25)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)


print('Accuracy on train data using Gini:',accuracy_score(y_true=y_train,y_pred=classifier.predict(X_train)))
print('Accuracy on test data using Gini:',accuracy_score(y_true=y_train,y_pred=y_pred))

classifier_entropy = DecisionTreeClassifier(criterion='entropy')
classifier_entropy.fit(X_train, y_train)
y_pred_entropy= classifier_entropy.predict(X_test)
print('Accuracy on train data using entropy:',accuracy_score(y_true=y_train,y_pred=classifier_entropy.predict(X_train)))
print('Accuracy on test data using entropy:',accuracy_score(y_true=y_test,y_pred=y_pred_entropy))

classifier_entropy1.fit(X_train,y_train) 
y_pred_entropy1 = classifier.entropy1.predict(X_test)
print('Accuracy on train data using entropy:',accuracy_score(y_true=y_train,y_pred=classifier_entropy1.predict(X_train)))
print('Accuracy on test data using entropy:',accuracy_score(y_true=y_test,y_pred=y_pred_entropy1))

dot_data = StringIO()
export_graphviz(classifier, out_file = dot_data, filled = True, rounded = True, special_characters =True,
                feature_names=data.feature_names, class_names = data.target_names)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())