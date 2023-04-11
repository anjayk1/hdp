"""Okay bro"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from flask import Flask
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    # upload heart dataset (1988)
    df = pd.read_csv("heart(version 1).csv")

    print(list(df))
    x = df.drop(['target', 'sex'], axis=1)
    y = df["target"]
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2)
    modelLogistic = LogisticRegression()
    modelLogistic.fit(x_train,y_train)
    y_pred= modelLogistic.predict(x_test)
    print(x_test)
    print(modelLogistic)
    print(y_pred)