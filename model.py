import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

dat = pd.read_csv('data.csv').drop('Unnamed: 0', axis = 1)

x = dat.drop('stroke', axis=1)
y = dat['stroke']

oversample = SMOTE()
x, y = oversample.fit_resample(x, y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier().fit(x_train, y_train)
y_pred = clf.predict(x_test)

print('Model accuracy score with criterion gini index: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

pickle.dump(clf, open('stroke.pkl', 'wb'))