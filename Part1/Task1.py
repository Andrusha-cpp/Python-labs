import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.exp(np.cos(x)) + np.log(np.cos(0.6 * x)**2 + 1) * np.sin(x)
h = lambda x: -np.log((np.cos(x) + np.sin(x))**2 + 2.5) + 10

x_d = np.linspace(-360, 360, 1000)
x_r = np.radians(x_d)
y1 = f(x_r)
y2 = h(x_r)

plt.plot(x_d, y1, label="f(x)", color="blue")
plt.plot(x_d, y2, label="h(x)", color="red")

plt.title("Graphics")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()