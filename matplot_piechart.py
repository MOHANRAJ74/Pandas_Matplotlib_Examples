import matplotlib.pyplot as mp
import numpy as np

students=np.array(["Arun","Bala","Dinesh","Elango","Kumar","Raja","Siva","Velu"])
marks=np.array([85,37,95,53,99,75,64,88])
exp=np.array([0,0,0.1,0,0,0,0,0])
mp.pie(marks, labels=students,autopct='%1.2f%%', explode=exp)

mp.title("Student Marks")

mp.show()