import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns

#importation de dataset
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
test_y =  pd.read_csv('gender_submission.csv')
#print(test)
#print(train)

#determination dex x et y
train_x = pd.get_dummies(train[['Pclass','Sex','Age','SibSp','Parch','Fare']])
train_y = train['Survived']
test_x = pd.get_dummies(test[['Pclass','Sex','Age','SibSp','Parch','Fare']])
#print(train_x)

#elimination de case vide
train_x=train_x.fillna(train_x.mean())
train_x

test_x=test_x.fillna(test_x.mean())

#entrainement de modele
for column in train_x.columns:
    train_x[column] = (train_x[column] - train_x[column].min()) / (train_x[column].max() - train_x[column].min())    

#print(train_x)

#strandilization（test）
for column in test_x.columns:
    test_x[column] = (test_x[column] - test_x[column].min()) / (test_x[column].max() - test_x[column].min())    


#faire l'agoritme de plus proche voisin
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(train_x,train_y)
predictions = model.predict(test_x)

#affichage de precision, recall,f1-sore et suport pour knn
from sklearn.metrics import classification_report

print(classification_report(test_y['Survived'], predictions))
