import matplotlib.pyplot as mp
import numpy as np

months=np.array(["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
rain=np.array([60,55,80,52,91,50,65,75,43,64,73,43])

mp.plot(months,rain)

mp.xlabel("Months")
mp.ylabel("Rain")

mp.title("Rainfall in a Year")

mp.show()