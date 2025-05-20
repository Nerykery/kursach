import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)
y = (3 * x) / (x**2 - 9)

plt.plot(x, y)
plt.show()