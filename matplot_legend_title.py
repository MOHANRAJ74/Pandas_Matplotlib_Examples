import matplotlib.pyplot as mp
import numpy as np

a=np.arange(5)
b=[2,4,6,8,10]
c=[5,6,7,8,9]

fig=mp.figure()
ax=mp.subplot()

ax.plot(a,b, 'k--',label="Frequency")
ax.plot(a,c,'k:',label="Period")

ax.legend(loc="upper center", fontsize='xx-large')

mp.title("Frequncy Of a Signal")

mp.show()