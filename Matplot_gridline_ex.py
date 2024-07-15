import matplotlib.pyplot as mp
import pandas as pd

cric={ "Cricket_Bat":["BAS","SS","SG","MRF","TON","PUMA","CEAT"],
       "MRP":[2000,2500,2900,3340,3700,4000,4200],
       "WEIGHT":[900,990,1050,1150,1200,1250,1300]
    }

dataframe=pd.DataFrame(cric)

mp.plot(dataframe["Cricket_Bat"],dataframe["WEIGHT"])

mp.grid()

mp.show()

