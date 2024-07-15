import pandas as pd
import os
import datetime as dt
import numpy as np
def getFilpath(filename):
    currentDir= os.getcwd()
    fullPath= os.path.join(currentDir, filename)
    return fullPath

df = pd.read_csv(getFilpath('G:\\AWS\\studs.csv'))

print("<-------All Values:--------->")
print(df)
print("<-------First 5 Values:--------->")
print(df.head())
print("<-----------Dimension of Dataset------------>")
print(df.shape)
print("<--------------Columns------------------>")
print(df.info)
print("<------------Check Null and Sum------------->")
print(df.isnull().sum())
print("<---------------Descripe-------------->")
print(df.describe())
print("<--------Values Counts------------->")
print(df.value_counts())
print("<----------Fillna------------>")
print(df['FEB'].isnull().sum())
print("<-----------Sample------------->")
print(df.sample())
print("<------------Columns------------->")
print(df.columns)
print("<----------NS Smallest-----------------")
print(df.nsmallest(7,'FEB'))
print("<----------NS Largest-----------------")
print(df.nlargest(7,'FEB'))
print("<----------to CSV File--------->")
print(df.to_csv("output.csv",index=True))
