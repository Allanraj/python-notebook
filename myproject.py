#!/usr/bin/env python3
#homework5 - Reach
import matplotlib.pyplot as plt
import pandas as pd


def printme(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

iris = pd.read_csv('data/iris.data',
                  names=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

printme ("My Projectdataset", iris[:])
#printme ("My Projectdataset", iris.columns)
printme("correlation between fields", iris.corr().to_string())

