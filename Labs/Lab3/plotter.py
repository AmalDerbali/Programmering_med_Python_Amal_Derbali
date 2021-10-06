# try plotting sphere based on: 
# https://stackoverflow.com/questions/11140163/plotting-a-3d-cube-a-sphere-and-a-vector-in-matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(dpi=100)
ax = fig.gca(projection='3d')

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="green")
ax.set_title("Sphere")
plt.show()