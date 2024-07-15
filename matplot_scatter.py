import matplotlib.pyplot as mp

t1=[25,75,65,78,45,19,65,79]
t2=[62,14,75,63,45,25,33,21]

scoreRange=[10,20,30,40,50,60,70,80]

mp.scatter(t1,scoreRange, color='r')
mp.scatter(t2,scoreRange, color='b')

mp.xlabel("Team Score")
mp.ylabel("Score Range")

mp.show()