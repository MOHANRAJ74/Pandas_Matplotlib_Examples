import matplotlib.pyplot as mp
import numpy as np

students=np.array(["Arun","Bala","Dinesh","Elango","Kumar","Raja","Siva","Velu"])
marks=np.array([85,37,95,53,99,75,64,88])

mp.bar(students,marks)

mp.xlabel("Students")
mp.ylabel("MArks")

mp.title("Student Marks")

mp.show()