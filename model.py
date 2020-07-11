import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv('speed.csv')

# speed_50mph,bumpiness,skill,cc


df['speed_50mph'].fillna(0, inplace=True)
df['bumpiness'].fillna(df['bumpiness'].mean(), inplace=True)
df['skill'].fillna(df['skill'].mean(), inplace=True)
df['cc'].fillna(df['cc'].mean(), inplace=True)

X = df.iloc[:, :3]

print('df: \n\n ',df)
print('X :\n\n',X)

def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]


y = df['speed_50mph']
y = y.apply(lambda x : convert_to_int(x))

print('y: \n\n',y)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X, y)

pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[4, 2, 5]]))