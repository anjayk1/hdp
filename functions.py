"""Okay bro"""

import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


# upload heart dataset
df = pd.read_csv("heartdata/heart(version 1).csv")

#Linear Regression and Cholesterol Level
def lrchol(input):
    X = df['chol'].values
    y = df['target'].values
    regress = stats.linregress(X, y)
    slope, intercept = regress.slope, regress.intercept

    def myfunc(X):
        return slope * X + intercept

    per = 100 * (1-myfunc(input))

    return per

#Linear Regression and Blood Pressure
def lrbp(input):
    X = df['trestbps'].values
    y = df['target'].values
    regress = stats.linregress(X, y)
    slope, intercept = regress.slope, regress.intercept

    def myfunc(X):
        return slope * X + intercept

    per = 100 * (1 - myfunc(input))

    return per

#Logistic Regression and Age
def lrage(input):
    X = df[['age']]
    y = df['target']

    model = LogisticRegression()
    model.fit(X, y)

    new_person = {'age': input}

    probabilities = model.predict_proba([[new_person['age']]])
    prob = probabilities[0][1]
    hdpage = prob * 100
    hdpage = 100 - hdpage
    return hdpage

#Logistic Regression and Sex
def lrsex(input):
    X = df[['sex']]
    y = df['target']

    model = LogisticRegression()
    model.fit(X, y)

    new_person = {'sex': input}

    probabilities = model.predict_proba([[new_person['sex']]])
    prob = probabilities[0][1]
    hdpsex = prob * 100
    hdpsex = 100 - hdpsex
    return hdpsex

#Decision Tree and All Values
def dtree(a, b, c, d, e):
    X = df[['cp', 'age', 'sex', "trestbps", "chol"]].values
    y = df['target'].values

    model = DecisionTreeClassifier(
        max_depth=3, criterion='gini', min_samples_split=5)
    model.fit(X, y)

    f = 100 * (model.predict([[a, b, c, d, e]]))
    g = 100 - f
    return g
