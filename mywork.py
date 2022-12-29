import pandas as pd
import sklearn
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib 
dataset=pd.read_csv('monfichier.csv')


#determinier les x et y
X=dataset[['montant','genre','ponctialit','age']]
y=dataset['place']

#on subdiviser le dataset en 2 partie

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

#choisir l'algorythme
regresseur=LinearRegression()

#entrainer grace a la methode fit
regresseur.fit(X_train,y_train)

#enregistre le modele
joblib.dump(regresseur, 'model.pkl')

#predire ou faire le test
y_pred=regresseur.predict(X_test)

df=pd.DataFrame({
    'actuel valeur' :y_test,
    'valeurs predites':y_pred
})
print(df)