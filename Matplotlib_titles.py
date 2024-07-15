import matplotlib.pyplot as mp
import pandas as pd

data={
    "Cricket_bat": ["SG","BAS","MRF","CEAT","NIKE","ADIDAS","PUMA"],
    "MRP":[2000,3000,4000,5000,6000,7000,8000],
    "Weight":[900,990,1100,1260,1300,1310,1350]
    }

dataframe=pd.DataFrame(data)

mp.plot(dataframe["MRP"],dataframe["Weight"])

mp.xlabel("Best Price(INR)")
mp.ylabel("Weight in Grams")

mp.title(label="Price and Weight", loc='right')

mp.show()
