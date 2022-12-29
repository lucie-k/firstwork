import pandas as pd
import joblib

test=[[55,2,1,35]]

model=joblib.load('model.pkl')

print(model.predict(test))