import numpy as np
import matplotlib.pyplot as plt

# making fake data
x = np.linspace(0, 2)
y = np.linspace(0, 2)
c = x[:,np.newaxis] * y
c2 = np.flipud(c)

# plot
fig, ax = plt.subplots(1, 1)
cont1 = ax.contour(x, y, c, colors='b')
cont2 = ax.contour(x, y, c2, colors='r')
cont1.clabel(cont1.levels)
cont2.clabel(cont2.levels)
plt.show()