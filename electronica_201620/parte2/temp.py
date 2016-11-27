import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("final_PID.csv", delimiter = ",")

time = data[:,0]
error = data[:,3]
plt.plot(time, error)
plt.xlabel("Tiempo (min)")
plt.ylabel("Error ($^\circ$C)")
plt.grid()
plt.savefig("final_PID.pdf")
