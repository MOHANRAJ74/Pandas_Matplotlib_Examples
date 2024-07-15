import matplotlib.pyplot as mp
import pandas as pd

data ={
    "Cricket Bat ":["BAS","RBK","Sparton","MRF","PUMA","TON","SS"],
    "MRP": [1700,1900,2100,2300,2500,2700,3000],
    "Weight_Grams": [900,1000,1100,1150,1150,1200,1300]
}

dataframe=pd.DataFrame(data)

mp.plot(dataframe["MRP"], dataframe["Weight_Grams"])

mp.show()