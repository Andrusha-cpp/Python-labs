import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 5 / (x**2 - 9)

x1 = np.linspace(-10, -3.01, 100) #remove 3 and -3 from graphic
x2 = np.linspace(-2.99, 2.99, 100)
x3 = np.linspace(3.01, 10, 100)

y1 = f(x1)
y2 = f(x2)
y3 = f(x3)

plt.plot(x1, y1, color="red")
plt.plot(x2, y2, color="red")
plt.plot(x3, y3, color="red")

plt.xlabel("x")
plt.ylabel('y')
plt.ylim(-30, 30)
plt.show()