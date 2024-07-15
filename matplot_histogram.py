import matplotlib.pyplot as mp
import numpy as np

arr=np.array([50,56,45,78,64,65,35,45,95,70,46])

mp.hist(arr,bins=[0,10,20,30,40,50,60,70,80,90,100])

mp.xlabel("Marks")
mp.ylabel("Students")

mp.show()