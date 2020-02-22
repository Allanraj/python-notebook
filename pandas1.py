#!/usr/bin/env python3
#homework5 - Advanced
import matplotlib.pyplot as plt
import pandas as pd


def printme(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

insurance = pd.read_csv('data/insurance.csv')

printme("insurance dataframe", insurance.to_string())
printme("insurance dataframe", insurance.columns)
printme("insurance dataframe", insurance.info())
printme("insurance dataframe", insurance.describe().to_string())

printme("age field", insurance['age'])
printme("imp 3 fields", insurance[['age','children','charges']])

printme("insurance dataframe", insurance.loc[0:4, ['age', 'children', 'charges']])
printme("Average value", insurance["charges"].mean())
printme("Min value", insurance["charges"].min())
printme("Max value", insurance["charges"].max())

#printme("Selecting age and sex of the person that paid 10797.3362 ", (insurance[['Sex', 'Age']] ) & (insurance.loc[insurance['charges'] == 10797.3362]))

tempvalue = insurance.loc[insurance['charges'] == 10797.3362]
print (tempvalue[['age', 'sex']])

print ("Age of the person who paid max charge", insurance['age'] , insurance["charges"].max())

print ("insured people we have for each region", insurance.groupby(['region']).size())
printme("NO of Insured people are children", insurance[insurance['children'] > 0].count())

printme("correlation between fields", insurance.corr().to_string())


plt.close()

