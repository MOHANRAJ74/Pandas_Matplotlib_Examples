import matplotlib.pyplot as mp
import matplotlib.pyplot as plt
import pandas
import pandas as pd

data ={
        "Criket_Bat":["BAS","TON","MRF","SG","SS","CEAT","HERO"],
        "MRP":[1000,2000,2200,2700,3200,3700,4320],
        "Weight":[900,990,1100,1200,1400,1600,1900]
    }
dataframe=pd.DataFrame(data)

mp.plot(dataframe["MRP"],dataframe["Weight"])

mp.xlabel("Bat Price (INR)")
mp.ylabel("Bat Weight (Grams)")

plt.show()