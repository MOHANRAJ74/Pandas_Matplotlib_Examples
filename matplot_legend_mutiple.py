import numpy as np
import matplotlib.pyplot as mp

a1=[100,102,99,101,101,100,102]
a2=[90,95,102,104,105,103,109]
a3=[110,115,100,105,100,98,95]

mp.plot(a1, label="Company 1")
mp.plot(a2, label="Company 2")
mp.plot(a3, label="Company 3")

mp.legend()

mp.show()