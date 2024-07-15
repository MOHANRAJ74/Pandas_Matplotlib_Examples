import matplotlib.pyplot as mp
import numpy as np

a=np.arange(5)
b=[2,4,6,8,10]
c=[5,6,7,8,9]

fig=mp.figure()
ax=mp.subplot()

ax.plot(a,b,'k--',label='Frequency')
ax.plot(a,c,'k:',label='Period')

legend =ax.legend(loc='upper center')

legend.get_frame().set_facecolor('red')

mp.title('Frequency of a Signal')

mp.show()