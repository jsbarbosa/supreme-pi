import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("KP.csv", delimiter = ",")

xs = [5, 20, 28, 39, 50, 59, 67, 72, 80]
ys = [3, 25, 15, 13, 11, 8, 5.1, 3, 2]
kps = ["$\infty$", "1", "10", "20", "50", "100", "1000", "10000", "100000"]

time = data[:,0]
error = data[:,3]
plt.plot(time, error)
plt.xlabel("Tiempo (min)")
plt.ylabel("Error ($^\circ$C)")
plt.grid()

for i in range(len(xs)):
    plt.text(xs[i], ys[i], kps[i])


plt.savefig("KP.pdf")
